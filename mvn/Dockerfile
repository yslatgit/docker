FROM centos:7.6.1810

ADD jdk1.8.0_191.tgz /usr/local/
ADD apache-maven-3.6.1.tar.gz /usr/local/
#修改配置文件
ADD settings.xml /usr/local/apache-maven-3.6.1/conf/

ENV JAVA_HOME /usr/local/jdk1.8.0_191/
ENV M2_HOME /usr/local/apache-maven-3.6.1/
ENV M2 $M2_HOME/bin
ENV MAVEN_OPTS -Xms256m -Xmx512m
ENV PATH $PATH:$JAVA_HOME/bin:$MAVEN_HOME/bin:$M2_HOME:$M2