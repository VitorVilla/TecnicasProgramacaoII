import java.util.Map;

public class Lagarto extends Algoritmo {

    @Override
    public Map<String, String> executar(Tipo pTipo) {
        switch (pTipo) {
            case PAPEL -> valor = "Ganhou!. Lagarto come o papel!";
            case TESOURA -> valor = "Perdeu! Tesoura corta o lagarto!";
            case PEDRA -> valor = "Perdeu! Pedra esmaga o Lagarto!";
            case LAGARTO -> valor = "Empata! Lagarto empata com lagarto!";
            case SPOCK -> valor = "Ganhou! Lagarto envenena o Spock!";
            default -> valor = "Empatou! Opção inválida!";
        }

        resultado.put(KEY, valor);
        return resultado;
    }
}
