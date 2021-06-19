# Frontend
The frontend is as a flask app, which get the http API requests from client and these requesta re transformed to nameko RPC calls, using [nameko standalon RPC](https://nameko.readthedocs.io/en/stable/built_in_extensions.html). which talks to the message broker.
