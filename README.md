# Boardgame Recommender Projekt
A Recommender for Boardgame based on [boardgamegeeks.com](http://www.boardgamegeeks.com).

Details descriped in following [Blog](https://boardgamerecommender.wordpress.com/).

## Setup

As setup process it is needed to run analytics/get data.ipynb to get all the needed data. You will need "boardgame-ranks.csv" that can be downloaded from boardgamegeeks.com.
Then you need to run "Recomender.ipynb" to create the needed recommendation files.
Afterwards you can use docker-compose.yml to run the containers.

## Folders
- data: contains all data generated in the project.
- analytics: test the api and get the needed data.
- reco: the recommender files including the reco_api REST-API.
- html: the web-frontend.
- proxy: the configuration for the nginx proxy-server container.
