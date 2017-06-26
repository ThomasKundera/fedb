<TeXmacs|1.99.2>

<style|<tuple|article|french>>

<\body>
  <\doc-data|<doc-title|�nergie potentielle sur une Terre oblate en
  rotation>|<doc-author|<\author-data|<author-name|TK>>
    \;
  <|author-data>
    \;
  <|author-data>
    \;
  </author-data>>>
    \;
  </doc-data>

  <section|Pr�sentation du probl�me>

  Le rayon �quatorial de la Terre est plus grand que son rayon polaire de
  plus de <math|20 km>. Comment se fait-il que l'�quateur ne soit pas une
  �norme montage?

  La gravit� devrait faire tomber l'eau hors de l'�quateur vers les p�les, or
  ce n'est pas le cas.

  �l'inverse, certains pensent que cette force centrifuge devrait disperser
  la Terre dans l'espace.

  Qu'en est-il vraiment?

  Le calcul est essentiellement une reprise de
  <inactive|<hlink|http://www.cns.gatech.edu/PHYS-4421/lautrup/book/shapes.pdf|>>,
  \ Physics of Continuous Matter, Benny Lautrup.

  <section|Consid�rations g�n�rales et m�thode>

  Intuitivement, on comprend bien que ce qui permet de r�soudre la
  contradiction apparente est la pseudo-force centrifuge qui vient modifier
  le potentiel gravitationnel en ajoutant un terme sp�cifique.

  Il va donc falloir calculer la valeur de ce terme additionnel, et v�rifier
  que la surface de la Terre � \S<nbsp>altitude constante<nbsp>\T est bien
  une iso-potentielle de la somme de ces deux potentiels (ce qui est
  �quivalent � d�montrer que la r�sultante des forces est normale � la
  surface).

  Cependant, l'effet est tr�s faible, et le d�placement des masses caus�e par
  l'�largissement � l'�quateur modifie la forme du potentiel gravitationnel
  d'un ordre de grandeur �quivalent: on ne peut donc pas n�gliger cet effet
  non plus.

  Cela conduit donc � un calcul assez complexe, que je reprends de Benny
  Lautrup, faute de pouvoir donner une valeur r�aliste � partir d'un calcul
  simplifi� comme je l'esp�rais (le calcul simple est effectu� dans la m�me
  r�f�rence, il minimise la r�alit� du d�placement d'un facteur deux
  environ).

  <section|Calculs>

  <subsection|Petites choses utiles>

  <subsubsection|Champs de potentiel gravitationnel � la surface d'une
  ellipso�de de r�volution>

  \;

  \;

  <section|G�om�trie de la Terre et forces en pr�sence>

  La Terre sera assimil�e pour ce calcul � une ellipso�de de r�volution
  oblate<\footnote>
    Les donn�es suivantes proviennent de <inactive|<hlink|https://fr.wikipedia.org/wiki/Terre|>>,
    j'ai choisi la notation anglaise des nombres (usage du point d�cimal et
    non de la virgule).
  </footnote> de rayon polaire <math|r<rsub|p>=6356.752 km> et de rayon
  �quatorial <math|r<rsub|e>=6378.137 km>.

  Les deux forces � consid�rer sont bien s�r la gravit� et les pseudo-forces
  centrifuges dues � la rotation de la Terre.

  L'une des difficult�s de ce calcul est que les variations de forces sont
  tr�s faibles, et que certaines approximations tentantes ne peuvent �tre
  faites.

  La force de gravitation est une force centrale:

  <math|<wide|P|\<vect\>>=-mg<wide|r|\<vect\>>>

  A priori, <math|g> d�pend de l'altitude, selon l'�quation de la gravitation
  universelle:

  <math|g=<frac|GM<rsub|t>|r<rsup|2>>>, avec <math|G> constante
  gravitationnelle et <math|M<rsub|t>>, la masse de la Terre.

  Cependant:

  <math|<frac|g<around*|(|r<rsub|p>|)>|g<around*|(|r<rsub|e>|)>>=<frac|<frac|GM<rsub|t>|r<rsub|p><rsup|2>>|<frac|GM<rsub|t>|r<rsub|e><rsup|2>>>=<frac|r<rsup|2><rsub|e>|r<rsup|2><rsub|p>>=1.0067>,
  la gravit� varie de moins de <math|7> pour mille sur la zone d'int�r�t: on
  la consid�rera comme constante.

  La pseudo-force centrifuge a pour expression:

  <math|F=mv<rsup|2>/<wide|r<rsub|r>|\<vect\>>>

  Le vecteur unitaire <math|<wide|r<rsub|r>|\<vect\>>> est perpendiculaire �
  l'axe de rotation, il ne peut �tre confondu avec le vecteur unitaire en
  coordonn�es sph�riques.

  \;

  <section|Calcul>

  \;

  \;

  <section|Graphe>

  \;

  <section|Notes et r�f�rences>

  \;
</body>

<\initial>
  <\collection>
    <associate|page-type|a4>
    <associate|par-hyphen|normal>
  </collection>
</initial>

<\references>
  <\collection>
    <associate|FigEigthInches|<tuple|6|?>>
    <associate|FigPinHole|<tuple|10|?>>
    <associate|FigShape1|<tuple|1|?>>
    <associate|Fighl|<tuple|9|?>>
    <associate|Figure 1|<tuple|2|?>>
    <associate|SectVanishing|<tuple|3|?>>
    <associate|auto-1|<tuple|1|1>>
    <associate|auto-10|<tuple|7|2>>
    <associate|auto-11|<tuple|2.5|2>>
    <associate|auto-12|<tuple|3|2>>
    <associate|auto-13|<tuple|3.1|2>>
    <associate|auto-14|<tuple|3.2|2>>
    <associate|auto-15|<tuple|3.2.1|3>>
    <associate|auto-16|<tuple|1|3>>
    <associate|auto-17|<tuple|3.2.2|3>>
    <associate|auto-18|<tuple|3.3|3>>
    <associate|auto-19|<tuple|3.3.1|4>>
    <associate|auto-2|<tuple|2|1>>
    <associate|auto-20|<tuple|3.3.2|4>>
    <associate|auto-21|<tuple|2|4>>
    <associate|auto-22|<tuple|3.4|4>>
    <associate|auto-23|<tuple|3|5>>
    <associate|auto-24|<tuple|3.5|5>>
    <associate|auto-25|<tuple|4|?>>
    <associate|auto-26|<tuple|4.1|?>>
    <associate|auto-27|<tuple|4.2|?>>
    <associate|auto-28|<tuple|4|?>>
    <associate|auto-29|<tuple|4.3|?>>
    <associate|auto-3|<tuple|3|1>>
    <associate|auto-30|<tuple|5|?>>
    <associate|auto-31|<tuple|4.4|?>>
    <associate|auto-32|<tuple|6|?>>
    <associate|auto-33|<tuple|4.4.1|?>>
    <associate|auto-34|<tuple|4.4.2|?>>
    <associate|auto-35|<tuple|4.4.3|?>>
    <associate|auto-36|<tuple|4.4.4|?>>
    <associate|auto-37|<tuple|4.4.5|?>>
    <associate|auto-38|<tuple|4.4.6|?>>
    <associate|auto-39|<tuple|7|?>>
    <associate|auto-4|<tuple|3.1|1>>
    <associate|auto-40|<tuple|8|?>>
    <associate|auto-41|<tuple|5|?>>
    <associate|auto-42|<tuple|5.1|?>>
    <associate|auto-43|<tuple|5.2|?>>
    <associate|auto-44|<tuple|9|?>>
    <associate|auto-45|<tuple|5.3|?>>
    <associate|auto-46|<tuple|5.4|?>>
    <associate|auto-47|<tuple|5.4.1|?>>
    <associate|auto-48|<tuple|5.4.2|?>>
    <associate|auto-49|<tuple|10|?>>
    <associate|auto-5|<tuple|3.1.1|1>>
    <associate|auto-50|<tuple|5.5|?>>
    <associate|auto-51|<tuple|5.5.1|?>>
    <associate|auto-52|<tuple|11|?>>
    <associate|auto-53|<tuple|13|?>>
    <associate|auto-54|<tuple|13|?>>
    <associate|auto-6|<tuple|4|2>>
    <associate|auto-7|<tuple|5|2>>
    <associate|auto-8|<tuple|6|2>>
    <associate|auto-9|<tuple|7|2>>
    <associate|cite_ref-Lyons_5-2|<tuple|2.2|?>>
    <associate|eq2|<tuple|3.3.2|4>>
    <associate|eqata|<tuple|4|?>>
    <associate|eqd|<tuple|1|?>>
    <associate|eqda|<tuple|1|?>>
    <associate|eqdb|<tuple|3|?>>
    <associate|eqhcircle|<tuple|9|?>>
    <associate|eqhda|<tuple|5|?>>
    <associate|eqhl|<tuple|8|?>>
    <associate|eqhp|<tuple|7|?>>
    <associate|eqhr|<tuple|6|?>>
    <associate|eqmmp|<tuple|10|?>>
    <associate|eqmpr|<tuple|10|?>>
    <associate|figatana|<tuple|5|?>>
    <associate|figflatflat|<tuple|1|?>>
    <associate|fighorizonplot|<tuple|2|?>>
    <associate|figmathorizon|<tuple|1|?>>
    <associate|figspacecurve|<tuple|1|?>>
    <associate|footnote-1|<tuple|1|?>>
    <associate|footnr-1|<tuple|1|?>>
    <associate|heq|<tuple|9|?>>
  </collection>
</references>

<\auxiliary>
  <\collection>
    <\associate|figure>
      <tuple|normal||<pageref|auto-9>>
    </associate>
    <\associate|toc>
      <vspace*|1fn><with|font-series|<quote|bold>|math-font-series|<quote|bold>|1<space|2spc>Pr�sentation
      du probl�me> <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-1><vspace|0.5fn>

      <vspace*|1fn><with|font-series|<quote|bold>|math-font-series|<quote|bold>|2<space|2spc>Consid�rations
      g�n�rales et m�thode> <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-2><vspace|0.5fn>

      <vspace*|1fn><with|font-series|<quote|bold>|math-font-series|<quote|bold>|3<space|2spc>Calculs>
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-3><vspace|0.5fn>

      <with|par-left|<quote|1tab>|3.1<space|2spc>Petites choses utiles
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-4>>

      <with|par-left|<quote|2tab>|3.1.1<space|2spc>Champs de potentiel
      gravitationnel � la surface d'une �lipso�de de r�volution
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-5>>

      <vspace*|1fn><with|font-series|<quote|bold>|math-font-series|<quote|bold>|4<space|2spc>G�om�trie
      de la Terre et forces en pr�sence> <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-6><vspace|0.5fn>

      <vspace*|1fn><with|font-series|<quote|bold>|math-font-series|<quote|bold>|5<space|2spc>Calcul>
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-7><vspace|0.5fn>

      <vspace*|1fn><with|font-series|<quote|bold>|math-font-series|<quote|bold>|6<space|2spc>Graphe>
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-8><vspace|0.5fn>

      <vspace*|1fn><with|font-series|<quote|bold>|math-font-series|<quote|bold>|7<space|2spc>Notes
      et r�f�rences> <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-10><vspace|0.5fn>
    </associate>
  </collection>
</auxiliary>