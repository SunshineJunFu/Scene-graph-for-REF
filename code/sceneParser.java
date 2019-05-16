import edu.stanford.nlp.scenegraph.RuleBasedParser;
import java.io.*;
import edu.stanford.nlp.scenegraph.SceneGraph;
public class sceneParser{
    public static void main(String[] args)throws FileNotFoundException {
    String sentence = args[0]; //"A brown fox chases a white rabbit";

    RuleBasedParser parser = new RuleBasedParser();
    SceneGraph sg = parser.parse(sentence);
    //System.out.println(sg.toReadableString());
    //sg.toJSONString();
    PrintWriter pw = new PrintWriter(new File(args[1]+".txt"));
    pw.println(sg.toReadableString());
    pw.close();
}
}
