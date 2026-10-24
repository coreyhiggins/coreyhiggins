#!/usr/bin/env node
// Rewrite the releases block in README.md from real GitHub releases.
// Runs in Actions on a schedule and on demand, so the profile never goes stale.

import { writeFileSync, readFileSync } from "node:fs";

const USER = "coreyhiggins";
const REPOS = [
  "wynfall",
  "proofmark",
  "tanto",
  "blastradius",
  "grain",
  "jvm-shutdown-watchdog",
  "failsoft-webhook",
  "linux-deploy-toolkit",
  "service-health-monitor",
  "mcp-server-example",
  "accesspath",
];

const START = "<!-- releases:start -->";
const END = "<!-- releases:end -->";
const LIMIT = 8;

const token = process.env.GITHUB_TOKEN;
const headers = {
  Accept: "application/vnd.github+json",
  "User-Agent": "readme-updater",
  ...(token ? { Authorization: `Bearer ${token}` } : {}),
};

async function releasesFor(repo) {
  const url = `https://api.github.com/repos/${USER}/${repo}/releases?per_page=100`;
  const res = await fetch(url, { headers });
  if (res.status === 404) return [];
  if (!res.ok) {
    throw new Error(`${repo}: ${res.status} ${res.statusText}`);
  }
  const data = await res.json();
  return data
    .filter((r) => !r.draft)
    .map((r) => ({
      repo,
      name: r.name || r.tag_name,
      tag: r.tag_name,
      url: r.html_url,
      date: new Date(r.published_at).toISOString().slice(0, 10),
    }));
}

function render(entries) {
  if (entries.length === 0) {
    return "_No public releases yet._";
  }
  const lines = entries.map(
    (e) => `[${e.repo} ${e.tag}](${e.url}) &nbsp;·&nbsp; <sub>${e.date}</sub>`
  );
  return lines.join("\n\n");
}

const all = [];
for (const repo of REPOS) {
  try {
    all.push(...(await releasesFor(repo)));
  } catch (err) {
    console.error(`skipped ${repo}: ${err.message}`);
  }
}

all.sort((a, b) => (a.date < b.date ? 1 : a.date > b.date ? -1 : 0));

// One entry per project: the newest release. A wall of the same repo repeated
// reads as noise, and the reader wants to know what moved, not every tag.
const seen = new Set();
const latestPerRepo = [];
for (const e of all) {
  if (seen.has(e.repo)) continue;
  seen.add(e.repo);
  latestPerRepo.push(e);
}

const block = render(latestPerRepo.slice(0, LIMIT));

const path = "README.md";
const current = readFileSync(path, "utf8");
const a = current.indexOf(START);
const b = current.indexOf(END);
if (a === -1 || b === -1 || b < a) {
  console.error(`missing markers ${START} ... ${END} in ${path}`);
  process.exit(1);
}

const next =
  current.slice(0, a + START.length) + "\n" + block + "\n" + current.slice(b);

if (next === current) {
  console.log(`unchanged (${all.length} releases, showing ${Math.min(all.length, LIMIT)})`);
} else {
  writeFileSync(path, next, "utf8");
  console.log(`updated: ${all.length} releases, showing ${Math.min(all.length, LIMIT)}`);
  for (const e of all.slice(0, LIMIT)) console.log(`  ${e.repo} ${e.tag} ${e.date}`);
}
