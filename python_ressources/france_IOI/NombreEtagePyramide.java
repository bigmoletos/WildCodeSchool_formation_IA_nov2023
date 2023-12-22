package javaProjets;

import java.util.Scanner;

/**
 * @author franck Desmedt
 *
 */
public class NombreEtagePyramide {

	/**
	 * @description Département d'architecture : construction d'une pyramide Les
	 *              habitants adorent les constructions en forme de pyramide ; de
	 *              nombreux bâtiments officiels ont d'ailleurs cette forme. Pour
	 *              fêter les 150 ans de la construction de la ville, le gouverneur
	 *              a demandé la construction d'une grande et majestueuse pyramide à
	 *              l'entrée de la ville. Malheureusement, en ces périodes de
	 *              rigueur budgétaire, il y a peu d'argent pour ce projet. Les
	 *              architectes souhaitent cependant construire la plus grande
	 *              pyramide possible étant donné le budget prévu.
	 * 
	 *              Ce que doit faire votre programme: Votre programme doit d'abord
	 *              lire un entier : le nombre maximum de pierres dont pourra être
	 *              composée la pyramide. Il devra ensuite calculer et afficher un
	 *              entier : la hauteur de la plus grande pyramide qui pourra être
	 *              construite, ainsi que le nombre de pierres qui sera nécessaire.
	 *
	 * @return void
	 *
	 * @method main
	 * @class TestAlgo
	 * @version 1.0
	 * @date lundi 02 sept. 2019
	 * @see
	 *
	 **/

	public static void main(String[] args) {
		System.out.println("veuillez entrer le nombre de pierres");
		Scanner entrée = new Scanner(System.in);
		int nombreMaximumPierres = entrée.nextInt();
		int nombrePierres = 0;
		int hauteur = 1;

		while (nombrePierres + hauteur * hauteur <= nombreMaximumPierres) {
			nombrePierres = nombrePierres + hauteur * hauteur;
			hauteur = hauteur + 1;
		}
		entrée.close();
		System.out.println("nombre d'étages: " + (hauteur - 1));
		System.out.println("nombre pierres utilisées: " + nombrePierres);
		System.out.println("nombre pierres non utilisées: " + (nombreMaximumPierres - nombrePierres));
	}
}
