# Bachelor Thesis Galina Atamankina

1. To deploy to minikube, use the `kubernetes/local` folder.

2. To deploy in a cluster, use the `kubernetes/k8s_cluster` folder.

3. To run flask app locally, see `useful_commands/other_commands.sh` to export variables, apply migrations, adn run gunicorn.

4. To generate data, run `mock_data/generate_data.py` with the `-u base_url` argument specifying the URL to the app.

5. See postman collections for available APIs in the `postman` folder.

6. To run locust tests, export the `BASE_URL` environment variable and use `locust_tests\Makefile`.

7. To see experiment data and statistics, see the `statistics` folder.
