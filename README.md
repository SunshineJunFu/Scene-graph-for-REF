# Scene-graph-for-REF
Scene graph 

## [Stanford Scene Graph Parser](https://nlp.stanford.edu/software/scenegraph-parser.shtml)

### download files:
+ [CoreNLP 3.6.0](https://nlp.stanford.edu/software/stanford-corenlp-full-2015-12-09.zip)
+ [Scene Graph Parser](https://nlp.stanford.edu/projects/scenegraph/scenegraph-1.0.jar)
+ [json-simple](http://www.java2s.com/Code/Jar/j/Downloadjsonsimple111jar.htm)

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
System.out.println(sg.toJSON(0,null,null)); 
```

function: toReadableString()
```java
public String toReadableString() {
		StringBuilder buf = new StringBuilder();
		buf.append(String.format("%-20s%-20s%-20s%n", "source", "reln", "target"));
		buf.append(String.format("%-20s%-20s%-20s%n", "---", "----", "---"));
		for (SceneGraphRelation edge : this.relationList()) {
			buf.append(String.format("%-20s%-20s%-20s%n", edge.getSource(), edge.getRelation(), edge.getTarget()));
		}

		buf.append(String.format("%n%n"));
		buf.append(String.format("%-20s%n", "Nodes"));
		buf.append(String.format("%-20s%n", "---"));

		for (SceneGraphNode node : this.nodeList()) {
			buf.append(String.format("%-20s%n", node));
			for (SemanticConcept attr : node.getAttributes()) {
				buf.append(String.format("  -%-20s%n", attr));
			}
		}
		return buf.toString();
	}
```
