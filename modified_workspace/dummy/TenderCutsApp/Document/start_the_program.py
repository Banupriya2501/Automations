1) start appium  --chromedriver-executable /usr/bin/chromedriver
Note:version lower than 7
2) Go to directory and open subl . 
   [~/workspace/TenderCutsApp]
3) Run the project by
   [ env PYTHONPATH=./ python3 -m pytest --html=report.html -k tests -s -vvv]
4)adb devices

5)adb install "path to the build"