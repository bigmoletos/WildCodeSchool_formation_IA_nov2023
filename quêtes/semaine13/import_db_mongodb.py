# db.getCollection("restaurants").find({'Name': /^[bcd][eiou]/})


wget https://raw.githubusercontent.com/mongodb/docs-assets/primer-dataset/primer-dataset.json

mongoimport --db newdb --collection restaurants --file primer-dataset.json
