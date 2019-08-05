package edu.usc.inf558;
import org.apache.jena.rdf.model.*;
import java.io.FileOutputStream;

public class App 
{
    public static void main(String[] args)
    {
        Model model =
                ModelFactory.createDefaultModel();
        model.read(args[0]);
        ResIterator ri = model.listSubjects();
        try{
            model.write(new FileOutputStream(args[1]),
                    "Turtle");
        } catch (Exception e) {
            System.out.println(e);
        }
        while (ri.hasNext()){
            Resource r = ri.next();
            System.out.println(r.getURI() +" - " + r.listProperties().toList().size());
        }



    }
}
