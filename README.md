<img src="https://raw.githubusercontent.com/coreyhiggins/coreyhiggins/main/banner.svg" alt="Corey Higgins, founder and head of engineering at Wynfall Studios" width="100%">

<p>
I founded <a href="https://wynfall.dev">Wynfall Studios</a>. I train the Wynfall model family on GPUs I run myself, and I build the products around it: Sigel, Ken, and Nova. Writing, reasoning, code.
</p>

<p>
Most of that work stays closed. When a problem turns out to be general rather than ours, I publish the fix. Those tools are below.
</p>

<br>

## What I ship

<table>
<tr>
<td width="50%" valign="top">

### [blastradius](https://github.com/coreyhiggins/blastradius)

Sits in front of an agent's shell and answers one question before the command runs: how far does this reach?

File edits can be undone. `terraform destroy` cannot.

[![npm](https://img.shields.io/npm/v/@coreyhiggins/blastradius?style=flat-square&labelColor=0d1117&color=0b7285)](https://www.npmjs.com/package/@coreyhiggins/blastradius)
[![license](https://img.shields.io/badge/license-MIT-0b7285?style=flat-square&labelColor=0d1117)](https://github.com/coreyhiggins/blastradius/blob/main/LICENSE)

```
npx @coreyhiggins/blastradius install
```

</td>
<td width="50%" valign="top">

### [grain](https://github.com/coreyhiggins/grain)

Routes each prompt to the right discipline and injects only the matching guidance. Zero tokens on conversational turns.

Every claim is benchmarked, including the ones that failed.

[![npm](https://img.shields.io/npm/v/@coreyhiggins/grain?style=flat-square&labelColor=0d1117&color=0b7285)](https://www.npmjs.com/package/@coreyhiggins/grain)
[![license](https://img.shields.io/badge/license-MIT-0b7285?style=flat-square&labelColor=0d1117)](https://github.com/coreyhiggins/grain/blob/main/LICENSE)

```
npx @coreyhiggins/grain
```

</td>
</tr>
</table>

<br>

## Smaller things

Small, zero-dependency tools. Each one exists because something bit me once.

| | |
|---|---|
| [**proofmark**](https://github.com/coreyhiggins/proofmark) | Backtest engine whose defaults make self-deception expensive. Suppresses impossible results, tests every bar for lookahead, counts your trials. |
| [**tanto**](https://github.com/coreyhiggins/tanto) | Measured Windows performance tuning with reversible changes and evidence from your own machine. |
| [**jvm-shutdown-watchdog**](https://github.com/coreyhiggins/jvm-shutdown-watchdog) | Forces a wedged JVM to exit and reports which threads wedged it. |
| [**failsoft-webhook**](https://github.com/coreyhiggins/failsoft-webhook) | Posts alerts to a webhook without taking down the app sending them. |
| [**linux-deploy-toolkit**](https://github.com/coreyhiggins/linux-deploy-toolkit) | Versioned releases, atomic symlink swap, health check, automatic rollback. |
| [**service-health-monitor**](https://github.com/coreyhiggins/service-health-monitor) | Endpoint and systemd monitoring on a timer, with state-change alerts. |
| [**mcp-server-example**](https://github.com/coreyhiggins/mcp-server-example) | Dependency-free Model Context Protocol server over stdio. |

<br>

## Currently

- Running inference for the Wynfall model family on a GH200, and on two 3090s in the lab
- Building [Wynfall Desktop](https://wynfall.dev), the local-first app the models live in
- Writing down what actually broke, not what was supposed to work

<br>

## Elsewhere

[wynfall.dev](https://wynfall.dev) &nbsp;·&nbsp; [npm](https://www.npmjs.com/~coreyhiggins) &nbsp;·&nbsp; [X](https://x.com/coreywynfall) &nbsp;·&nbsp; [corey@wynfall.dev](mailto:corey@wynfall.dev)
