echo "Starting tests";

# start the environment
cd $WORKSPACE/TenderCutsApp/jenkins && /usr/local/bin/docker-compose down;
cd $WORKSPACE/TenderCutsApp/jenkins && /usr/local/bin/docker-compose build && /usr/local/bin/docker-compose up -d --force-recreate;

sleep 300;

/usr/bin/docker exec -t -u root $(/usr/bin/docker ps -aqf "name=appium") \
    sh -c "cd /test && py.test -s -vvv . --junitxml=/test/jenkins/jenkins.xml -k test_freshchat"
