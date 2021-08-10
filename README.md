# VAIT Melbourne Team - GovHack project

## Prerequisites

- [Python 3.8](https://www.python.org/downloads/ "Python download link").
  - For working on Backend code.
  - Also needed: [Poetry](https://python-poetry.org/ "Python Poetry").
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html "AWS CLI").
  - For loading AWS Credentials.
  - After installing AWS CLI, run `aws configure` to [set up your AWS credentials](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html "AWS CLI Configurations Basics").
- [Node 14](https://nodejs.org/en/download/ "NodeJS Download").
  - For working with Frontend code, and facilitating with the Serverless framework.
  - Also needed:
    - [Yarn v1](https://classic.yarnpkg.com/en/docs/install/ "Yarn download")
    - [Serverless CLI](https://www.serverless.com/framework/docs/getting-started/ "Serverless install")
  - Nice to have:
    - [`nvm`](https://nvm.sh/ "NVM"). A neat tool to have if you have multiple
    versions of Node installed on your machine.
- [Docker](https://www.docker.com "Docker").
  - Although we don't use Docker directly, we need it to package the Python dependencies.
  - For Mac and Windows, get [Docker Desktop](https://www.docker.com/products/docker-desktop "Docker Desktop")
  - For Linux, follow the steps [appropriate for your distro](https://docs.docker.com/engine/install/ "Install Docker engine")
  and follow the [post installation steps](https://docs.docker.com/engine/install/linux-postinstall/ "Docker Linux Post installation steps").

## Setup

Clone the repo, and follow the setup steps in each service `README.md` file.
