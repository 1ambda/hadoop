hadoop note
======

### Intro to Hadoop and MapReduce

Cloudera, Udacity

### Install on OSX

- "코드를 데이터가 있는 곳으로 보내자." 데이터의 양이 많아지면 유리
- 하둡은 scale up 이 아니라 scale out
- 관계형 테이블이 아닌 Key/Value
- 선언적 언어(SQL) 이 아닌 기능적 프로그래밍(MR)
- 온라인 처리가 아닌, 오프라인 배치 처리

"MR 로 작성하면, 1대에서 돌아가는 프로그램을 100대, 1000대에서 돌리는건 문제도 아니다."

### Hadoop Install on OSX

[Installation Guide](http://amodernstory.com/2014/09/23/installing-hadoop-on-mac-osx-yosemite/)

hdfs-site.xml 에 다음 추가. 폴더도 만들고

dfs.namenode.name.dir
file:/usr/local/Cellar//hadoop/hdfs/namenode

dfs.datanode.data.dir
file:/usr/local/Cellar//hadoop/hdfs/datanode

hstart, hstop
hadoop jar <example jar> pi 10 100

Resource Manager: http://localhost:50070
JobTracker: http://localhost:8088
Specific Node Information: http://localhost:8042

### Wordcount Sample Code

[Sample Code](https://hadoopi.wordpress.com/2013/05/25/setup-maven-project-for-hadoop-in-5mn/)

### Gradle

```gradle
dependencies {
    compile group: 'commons-collections', name: 'commons-collections', version: '3.2'
    compile('org.springframework.boot:spring-boot-starter:1.2.2.RELEASE')
    compile('org.apache.hadoop:hadoop-core:1.2.1')
   	compile('org.apache.hadoop:hadoop-common:2.6.0')
   	compile('org.apache.hadoop:hadoop-hdfs:2.6.0')
   	compile('org.apache.hadoop:hadoop-auth:2.6.0')

    testCompile group: 'junit', name: 'junit', version: '4.+'
}
```
