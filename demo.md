# Welcome to Gitpod

You're currently in a Textual app, running in a bash shell. At any time, you can press CTRL+C to exit this program. You can re-run it via `python3 cli.py`. You can also click the `+` sign, and create another shell instances while keeping this one open.

## Connecting to AWS 

This repository is meant to be connected with [Doppler](https://www.doppler.com/), and specifically uses [Dynamic Secrets](https://docs.doppler.com/docs/dynamic-secrets) to inject disposable AWS credentials.

This allows us to build and push Docker containers to an AWS Container Registry, given our working IAM role.

In fact, we can test that our AWS connection works within this repo by doing a:

```bash
$ aws sts get-caller-identity
```

This should show us who we're logged in as, and prove that we have credentials to authenticate with AWS.

## Building the Images

The images are built via the specifications in the Makefile. Just type in `make` in the default workspace directory. Fair warning, it takes tens of minutes.


