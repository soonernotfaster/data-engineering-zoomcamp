# Sharable concepts

- Difference between `CMD` and `ENTRYPOINT` in Dockerfile
- Removing something from git that you accidently added `git rm -r 01-docker-terraform/docker_intro/ny_taxi_postgres_data --cached`
- [Compose file reference](https://docs.docker.com/reference/compose-file/)
- How to setup an venv, install dependencies and persist them for others to use
- Interactive rebase. Share how accidently commiting a CSV file several commits ago can cause some pain
- .gitkeep
- How to apply the principle of least access to service accounts
 for example (roles/storage.objectCreator)
 - Rather than using a service account, it would make sense to use [OIDC](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect#defining-trust-conditions-on-cloud-roles-using-oidc-claims)
 - Setting up [OIDC](https://github.com/google-github-actions/auth) on a private repo to manage roles 
 - OIDC is then set up using more limited roles on the public repo 