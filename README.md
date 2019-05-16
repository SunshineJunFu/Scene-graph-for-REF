# Scene-graph-for-REF
Scene graph 

## [Stanford Scene Graph Parser](https://nlp.stanford.edu/software/scenegraph-parser.shtml)

### download two files:
+ [CoreNLP 3.6.0](https://nlp.stanford.edu/software/stanford-corenlp-full-2015-12-09.zip)
+ [Scene Graph Parser](https://nlp.stanford.edu/projects/scenegraph/scenegraph-1.0.jar)
### set classspath:
```bash
export CLASSPATH=.:/your path/stanford-corenlp-full-2015-12-09/*:
```
### Usage

You can either run the parser programmatically or in interactive mode through the command line.

To parse sentences interactively, put all the jar files from the CoreNLP distribution and the Scene Graph Parser jar into one directory and then run the following command from this directory.
```bash
java -mx2g -cp "*" edu.stanford.nlp.scenegraph.RuleBasedParser
```
Alternatively, you can also run the parser programmatically as following.
```java
import edu.stanford.nlp.scenegraph.RuleBasedParser;
import edu.stanford.nlp.scenegraph.SceneGraph;

String sentence = "A brown fox chases a white rabbit.";

RuleBasedParser parser = new RuleBasedParser();
SceneGraph sg = parser.parse(sentence);

//printing the scene graph in a readable format
System.out.println(sg.toReadableString()); 

//printing the scene graph in JSON form
//System.out.println(sg.toJSON()); 
```
