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

The `.ci.toml` and `.github/workflows/build-image.yml` are ready for this standalone repository. `ba build` also needs `GITHUB_TOKEN` locally to trigger and monitor the workflow. `ba pub` requires the `ba-test` namespace and Deployment to exist or be provisioned in the target cluster. The config does not define an Ingress or HPA.
