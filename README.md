# Local development environment for python data projects, with Docker

Code for the post: [Setting up local dev environment with Docker](https://www.startdataengineering.com/post/local-dev/)

## Pre-requisite

To run the code, you will need

1. [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/)
2. [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

Clone the git repo and run the ETL as shown below.

```bash
git clone https://github.com/josephmachado/local_dev.git
cd local_dev
make up
make ci # run tests and format code
make run-etl # run the ETL process
make down # spins down the containers
```

For more details, please read the post: [Setting up local dev environment with Docker](https://www.startdataengineering.com/post/local-dev/).
