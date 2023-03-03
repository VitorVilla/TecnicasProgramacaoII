import java.util.Map;

public class Tesoura extends Algoritmo{

    @Override
    public Map<String, String> executar(Tipo pTipo) {
        switch (pTipo) {
            case PAPEL -> valor = "Ganhou!. Tesoura corta o papel!";
            case TESOURA -> valor = "Empate! Tesoura empata com tesoura!";
            case PEDRA -> valor = "Perdeu! Pedra quebra tesoura!";
            case LAGARTO -> valor = "Ganhou! Tesoura corta lagarto!";
            case SPOCK -> valor = "Perdeu! Spock esmaga a tesoura!";
            default -> valor = "Empatou! Opção inválida!";
        }

        resultado.put(KEY, valor);
        return resultado;
    }
}
