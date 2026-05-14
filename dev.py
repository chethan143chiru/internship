sudo apt update
sudo apt install openjdk-21-jdk -y
java -version
sudo apt install maven -y
mvn -version
sudo apt install gradle -y
gradle -version




sudo apt update
sudo apt install maven -y
sudo apt install default-jdk -y
mvn -version
mkdir mymavenapp
cd mymavenapp
mvn archetype:generate \
-DgroupId=com.example \
-DartifactId=MyMavenApp \
-DarchetypeArtifactId=maven-archetype-quickstart \
-DinteractiveMode=false
ls -R
nano pom.xml
<project>
<modelVersion>4.0.0</modelVersion>
<groupId>com.example</groupId>
<artifactId>MyMavenApp</artifactId>
<version>1.0-SNAPSHOT</version>
<dependencies>
</dependencies>
</project>
mvn compile
mvn test
mvn package
<dependency>
<groupId>junit</groupId>
<artifactId>junit</artifactId>
<version>4.13.2</version>
<scope>test</scope>
</dependency>
mvn compile
mvn test
<build>
<plugins>
<plugin>
<groupId>org.apache.maven.plugins</groupId>
<artifactId>maven-compiler-plugin</artifactId>
<version>3.11.0</version>
<configuration>
<source>21</source>
<target>21</target>
</configuration>
</plugin>
</plugins>
</build>
mvn compile
mvn test
mvn clean




gradle -version
mkdir my-gradle-project
cd my-gradle-project
gradle init
mkdir -p src/main/java/com/example
touch src/main/java/com/example/App.java
package com.example;
public class App {
public static void main(String[] args) {
System.out.println("Hello Gradle!");
}
}
nano build.gradle
plugins {
id 'java'
id 'application'
}
group = 'com.example'
version = '1.0'
repositories {
mavenCentral()
}
dependencies {
testImplementation 'junit:junit:4.13.2'
implementation 'org.apache.commons:commons-lang3:3.14.0'
}
task hello {
doLast {
println 'Hello Gradle'
}
}
application {
mainClass = 'com.example.App'
}
gradle tasks
gradle build
gradle run




cd Desktop
mvn archetype:generate \
-DgroupId=com.example \
-DartifactId=demo-app \
-DarchetypeArtifactId=maven-archetype-quickstart \
-DinteractiveMode=false
cd demo-app
nano src/main/java/com/example/App.java
package com.example;
public class App {
public static void main(String[] args) {
System.out.println("Hello World!");
}
}
mvn clean package
java -cp target/demo-app-1.0-SNAPSHOT.jar com.example.App
gradle init
nano build.gradle
plugins {
    id 'java'
    id 'application'
}
group = 'com.example'
version = '1.0-SNAPSHOT'
repositories {
    mavenCentral()
}
dependencies {
    testImplementation 'junit:junit:4.13.2'
}
application {
    mainClass = 'com.example.App'
}
gradle build
gradle run




sudo apt update
sudo apt install docker.io -y
sudo systemctl start docker
sudo systemctl enable docker
sudo docker rm jenkins
sudo docker run -d \
-p 8080:8080 -p 50000:50000 \
--name jenkins \
jenkins/jenkins:lts

sudo docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword

Build Now
