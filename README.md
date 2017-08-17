# Example MPack for Ambari

## Building the Example MPack
Download ambari-mpack-example repository:

`git clone https://github.com/risdenk/ambari-mpack-example`

Build example mpack:

`./gradlew clean makePackage`

## Using the Example MPack
Stop Ambari server:

`ambari-server stop`

Deploy the Example MPack on Ambari server:

`ambari-server install-mpack --mpack=build/example-mpack-${version}.tar.gz -v`

Start Ambari server:

`ambari-server start`

##References
* https://cwiki.apache.org/confluence/display/AMBARI/Extensions
* https://cwiki.apache.org/confluence/display/AMBARI/Packaging+and+Installing+Custom+Services

