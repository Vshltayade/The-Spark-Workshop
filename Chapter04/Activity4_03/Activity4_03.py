from pyspark.sql import SparkSession
from Chapter01.utilities01_py.helper_python import create_session
from pyspark.ml.common import _java2py

if __name__ == "__main__":
    threads = 2
    session: SparkSession = create_session(threads, "PySpark <> JVM")
    python_rdd = session.sparkContext.range(0, 5)


    rdds = session.sparkContext.parallelize([germanSentence, englishSentence, frenchSentence])
    jRDD = session.sparkContext._jvm.SerDe.pythonToJava(rdds._jrdd, True)
    mapped = session.sparkContext._jvm.Exercise24_04.Exercise24_04.detectLanguageRDD(jRDD)


    java_rdd = session.sparkContext._jvm.SerDe.pythonToJava(python_rdd._jrdd, True)
    mapped_java_rdd = session.sparkContext._jvm.Exercise25_04.Exercise25_04.executeInScala(java_rdd)
    mapped_python_rdd = _java2py(session.sparkContext, mapped_java_rdd)
    print(mapped_python_rdd.collect())


