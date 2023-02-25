import java.util.Map;

public class Jokenpo {

    private Algoritmo algoritmo;

    public void setAlgoritmo(Algoritmo algoritmo) {
        this.algoritmo = algoritmo;
    }

    public void jogar(Tipo ptipo) {
        Map<String, String> map = algoritmo.executar(ptipo);
        System.out.println(map);
    }
}