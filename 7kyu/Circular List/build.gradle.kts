plugins {
    kotlin("jvm") version "1.7.0"
}

repositories {
    mavenCentral()
}

dependencies {
//    testImplementation(" org.hamcrest.CoreMatchers")
//import org.hamcrest.MatcherAssert.assertThat
//            "")
    testImplementation(kotlin("test"))
    testImplementation("org.hamcrest:hamcrest:2.2")
}

tasks.test {
    useJUnitPlatform()
}

