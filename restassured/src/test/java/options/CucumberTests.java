package options;

import org.junit.runner.RunWith;

import cucumber.api.CucumberOptions;
import cucumber.api.junit.Cucumber;

@RunWith(Cucumber.class)
@CucumberOptions(
		plugin = { "pretty", "html:target/cucumber-report" },
		glue = {"stepdefs"},
		features = {"src/test/features"}
		)
public class CucumberTests {}
