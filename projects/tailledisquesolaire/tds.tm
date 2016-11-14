<TeXmacs|1.99.2>

<style|<tuple|article|french>>

<\body>
  <\doc-data|<doc-title|Mesure de la taille apparente du disque
  solaire>|<doc-author|<\author-data|<author-name|TK>>
    \;
  <|author-data>
    \;
  <|author-data>
    \;
  </author-data>>>
    \;
  </doc-data>

  <section|Présentation du problème>

  <subsection|La question>

  En dépit des acquis de l'astronomie depuis 2500 ans, certains restent
  persuadés que la Terre est plate et supposent que le Soleil y tourne au
  dessus à faible altitude (quelques milliers de km).

  Quelle observation simple permettrait de trancher la question ?

  <subsection|Proposition>

  Si le Soleil ets proche, son déplacement au dessus de la Terre plate doit
  le faire apparaitre plus grand à midi que le matoin ou le soir. Une mesure
  de son diamètre apparent devrait donc permettre de confirmer ou infirmer
  cette hypothèse.

  <subsection|Modèles>

  <subsubsection|Le Globe dans le modèle héliocentrique>

  Le Soleil est de grande taille (1300000km de diamètre) et à grande distance
  (150000000km de la Terre): son diamètre apparent est quasi constant, il
  varie de manière saisonnière et fluctue entre 30' et 32'.

  <subsubsection|La Terre Plate>

  La Terre est un disque plat de quelques milliers de km de rayon, le Soleil
  tourne au dessus à quelques milliers de km de distance.

  La variation de diamètre apparent sera d'autant plsu grande que la Terre
  sera grande et le Soleil près. Nous choisirons donc une Terre petite (5000
  km de rayon) et un Soleil loin: 20000 km de distance. Des valeurs plus
  petitres pour al Terre sont irréalistes et plus grande pour le Soleil en
  contradiction avec les modèles platistes.

  <section|Analyse>

  <subsection|Modèle héliocentrique>

  On mesure entre 30' et 32' quelque que soit l'heure de la journée, on
  observe une légère variation annuelle.

  <subsection|Modèle platCoilmpu>

  Calcul de <math|d>, la distance au Soleil depuis un point d'observation
  <math|A> de latitude <math|\<varphi\>> et de longitude <math|\<lambda\>>,
  avec une Terre plate de rayon <math|R>, un Soleil à une altitude <math|h>
  et une latitude <math|\<varphi\><rsub|s>> à une heure <math|>t.

  La distance droite du point d'observation au Pôle Nord est de: <math|r=
  <frac|\<varphi\>|\<pi\>>R>.

  <subsubsection|Position du Soleil suivant l'heure (GMT)>

  le Soleil est à midi (12h, soit <math|>43200 s) à la longitude <math|0>, il
  se déplace ensuite pour faire un tour en 24h, soit <math|2\<pi\>> en
  <math|n<rsub|s>=86400> secondes, sa longitude est donc:
  <math|\<lambda\><rsub|s>= 2\<pi\><frac|t<around*|[|n<rsub|s>|]>|n<rsub|s>>+\<pi\>>.

  Sa distance droite au pôle Nord est de <math|r<rsub|s>=
  <frac|\<varphi\><rsub|s>|\<pi\>>R>.

  <subsubsection|Distance à la projection droite du Soleil sur le plan de la
  Terre>

  La projection du Soleil sur le plan de la Terre a pour coordonnées
  <math|P<rsub|s>=<around*|(|\<varphi\><rsub|s>,\<lambda\><rsub|s>|)>>

  En utilisant la loi des consinus <math|c<rsup|2>=a<rsup|2>+b<rsup|2>-2ab<math-tt|cos>\<gamma\>>,
  on peut écrire:

  <\eqnarray*>
    <tformat|<table|<row|<cell|d<rsup|2><rsub|d>>|<cell|=>|<cell|r<rsup|2>+r<rsub|s><rsup|2>-2r
    r<rsub|s><math-tt|cos><around*|(|\<lambda\><rsub|s>-\<lambda\>|)>>>|<row|<cell|d<rsub|d>>|<cell|=>|<cell|<sqrt|r<rsup|2>+r<rsub|s><rsup|2>-2r
    r<rsub|s><math-tt|cos><around*|(|\<lambda\><rsub|s>-\<lambda\>|)>>>>>>
  </eqnarray*>

  \;

  <subsubsection|Distance au Soleil>

  Théorème de Pythagore:

  <\eqnarray*>
    <tformat|<table|<row|<cell|d<rsup|2>>|<cell|=>|<cell|h<rsup|2>+d<rsup|2><rsub|d>>>|<row|<cell|d>|<cell|=>|<cell|<sqrt|h<rsup|2>+d<rsup|2><rsub|d>>>>>>
  </eqnarray*>

  <subsubsection|Variation de taille>

  Distance à deux temps de mesures: <math|d<around*|(|t<rsub|1>|)>> et
  <math|d<around*|(|t<rsub|2>|)>>\ 

  Lorsque les angles sont petits, on peut simplifier
  <math|<math-tt|atan><around*|(|\<alpha\>|)>\<approx\>\<alpha\>>, donc la
  variation de longueur <math|\<Delta\><rsub|l>> du diamètre apparent du
  Soleil peut s'écrire:

  <math|\<Delta\><rsub|l>=<frac|d<around*|(|t<rsub|1>|)>|d<around*|(|t<rsub|2>|)>>>

  <section|Mesures>

  <section|Conclusions>

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
    <associate|auto-10|<tuple|2.2.1|2>>
    <associate|auto-11|<tuple|2.2.2|2>>
    <associate|auto-12|<tuple|2.2.3|2>>
    <associate|auto-13|<tuple|2.2.4|2>>
    <associate|auto-14|<tuple|3|2>>
    <associate|auto-15|<tuple|4|3>>
    <associate|auto-16|<tuple|1|3>>
    <associate|auto-17|<tuple|3.2.2|3>>
    <associate|auto-18|<tuple|3.3|3>>
    <associate|auto-19|<tuple|3.3.1|4>>
    <associate|auto-2|<tuple|1.1|1>>
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
    <associate|auto-3|<tuple|1.2|1>>
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
    <associate|auto-4|<tuple|1.3|1>>
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
    <associate|auto-5|<tuple|1.3.1|1>>
    <associate|auto-50|<tuple|5.5|?>>
    <associate|auto-51|<tuple|5.5.1|?>>
    <associate|auto-52|<tuple|11|?>>
    <associate|auto-53|<tuple|13|?>>
    <associate|auto-54|<tuple|13|?>>
    <associate|auto-6|<tuple|1.3.2|2>>
    <associate|auto-7|<tuple|2|2>>
    <associate|auto-8|<tuple|2.1|2>>
    <associate|auto-9|<tuple|2.2|2>>
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
    <associate|heq|<tuple|9|?>>
  </collection>
</references>

<\auxiliary>
  <\collection>
    <\associate|toc>
      <vspace*|1fn><with|font-series|<quote|bold>|math-font-series|<quote|bold>|1<space|2spc>Présentation
      du problème> <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-1><vspace|0.5fn>

      <with|par-left|<quote|1tab>|1.1<space|2spc>La question
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-2>>

      <with|par-left|<quote|1tab>|1.2<space|2spc>Proposition
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-3>>

      <with|par-left|<quote|1tab>|1.3<space|2spc>Modèles
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-4>>

      <with|par-left|<quote|2tab>|1.3.1<space|2spc>Le Globe dans le modèle
      héliocentrique <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-5>>

      <with|par-left|<quote|2tab>|1.3.2<space|2spc>La Terre Plate
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-6>>

      <vspace*|1fn><with|font-series|<quote|bold>|math-font-series|<quote|bold>|2<space|2spc>Analyse>
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-7><vspace|0.5fn>

      <with|par-left|<quote|1tab>|2.1<space|2spc>Modèle héliocentrique
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-8>>

      <with|par-left|<quote|1tab>|2.2<space|2spc>Modèle plat
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-9>>

      <with|par-left|<quote|2tab>|2.2.1<space|2spc>Position du Soleil suivant
      l'heure (GMT) <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-10>>

      <with|par-left|<quote|2tab>|2.2.2<space|2spc>Distance à la projection
      droite du Soleil sur le plan de la Terre
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-11>>

      <with|par-left|<quote|2tab>|2.2.3<space|2spc>Distance au Soleil
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-12>>

      <with|par-left|<quote|2tab>|2.2.4<space|2spc>Variation de taille
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-13>>

      <vspace*|1fn><with|font-series|<quote|bold>|math-font-series|<quote|bold>|3<space|2spc>Mesures>
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-14><vspace|0.5fn>

      <vspace*|1fn><with|font-series|<quote|bold>|math-font-series|<quote|bold>|4<space|2spc>Conclusions>
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-15><vspace|0.5fn>
    </associate>
  </collection>
</auxiliary>