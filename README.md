# ba-python-demo

A dependency-free Python HTTP service for trying the `ba` configuration and build flow. It responds with JSON on `/`, `/healthz`, and `/readyz`.

## Run locally

```sh
cd services/ba-python-demo
python3 app.py
```

In another terminal:

```sh
curl http://localhost:8080/healthz
```

## Try `ba`

From the workspace root, `ba` discovers this service config with:

```sh
ba build ba-python-demo
ba pub ba-python-demo
```

The `.ci.toml` is configured for this standalone repository with `runtime.type = "auto"`. `ba build ba-python-demo` detects Go or Python from the source files and uses the matching local Docker build flow. This service is detected as Python from `app.py` and `requirements.txt`. It builds `dhi.io/colder219/ba-python-demo:<git-sha>`; add `--tag local` to use the `local` tag. Build does not push to the registry. `ba pub` requires the `ba-test` namespace and Deployment to exist or be provisioned in the target cluster. The config does not define an Ingress or HPA.
