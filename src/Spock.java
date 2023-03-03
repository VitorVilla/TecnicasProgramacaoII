import java.util.Map;

public class Spock extends Algoritmo{

    @Override
    public Map<String, String> executar(Tipo pTipo) {
        switch (pTipo) {
            case PAPEL -> valor = "Perdeu!. Papel refuta o Spock!";
            case TESOURA -> valor = "Ganhou! Spock esmaga a tesoura!";
            case PEDRA -> valor = "Ganhou! Spock vaporiza a pedra!";
            case LAGARTO -> valor = "Perdeu! Lagarto envenena Spock!";
            case SPOCK -> valor = "Empatou! Spock empata com spock!";
            default -> valor = "Empatou! Opção inválida!";
        }

        resultado.put(KEY, valor);
        return resultado;
    }
}
