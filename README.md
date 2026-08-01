# Corey Higgins

I run production Linux infrastructure and publish the tools that fall out of it.

Ubuntu and systemd, MySQL, staged deploys with a rollback I have actually tested, monitoring, and being the only person on call. Before this I ran a Linux VPS hosting business serving over a thousand client servers, which is where I learned that the boring parts are the parts that matter at 3am.

Everything here is something I use.

## blastradius

[**blastradius**](https://github.com/CoreyH32/blastradius) guards AI coding agents against shell commands that leave your machine.

Agent checkpointing covers file edits. Anthropic's own documentation says it does not cover bash, which is where `ssh`, `terraform`, `kubectl`, `docker compose down -v`, and `git push --force` live. An agent working from a stale Terraform state ran `terraform destroy` and took out a production database along with its snapshots. The source files were fine. That was never the problem.

It classifies a command on two axes, how far it reaches and whether it destroys anything, and only interrupts on the intersection. `kubectl get pods` is remote and harmless. `rm -rf ./build` is destructive and local. Neither deserves a prompt. Custom rules can only escalate and never allowlist, because the agent being guarded can write files.

Zero dependencies. Installs as a Claude Code plugin.

## Also published

| | |
|---|---|
| [linux-deploy-toolkit](https://github.com/CoreyH32/linux-deploy-toolkit) | Versioned releases, atomic symlink swap, health check, automatic rollback |
| [jvm-shutdown-watchdog](https://github.com/CoreyH32/jvm-shutdown-watchdog) | Forces a wedged JVM to exit and names the threads that wedged it |
| [failsoft-webhook](https://github.com/CoreyH32/failsoft-webhook) | Webhook alerting that cannot block, throw, or hold the process open |
| [service-health-monitor](https://github.com/CoreyH32/service-health-monitor) | Endpoint and unit checks on a timer, alerting on state change rather than every run |
| [mcp-server-example](https://github.com/CoreyH32/mcp-server-example) | Dependency-free Model Context Protocol server over stdio |

Georgia, US · corey@wynfall.dev
