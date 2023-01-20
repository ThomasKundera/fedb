<TeXmacs|1.99.2>

<style|<tuple|article|old-spacing|french>>

<\body>
  <\doc-data|<doc-title|Où l'on tente de pendre une corde à
  l'ISS>|<doc-author|<\author-data|<author-name|TK>>
    \;
  <|author-data>
    \;
  <|author-data>
    \;
  </author-data>>>
    \;
  </doc-data>

  <section|Introduction>

  Peut-on faire pendre une corde depuis l'ISS jusqu'au sol? À quelles
  conditions?

  <section|Présentation du problème>

  <subsection|Description>

  On suppose que depuis l'ISS en orbite, on arrive à faire pendre une corde
  vers le sol, qui suivent la même vitesse angulaire que la station. Comment
  va se comporter la corde? L'ISS? Peut-on aller jusqu'au sol?

  <subsection|Schéma et notations associées>

  L'ISS est à une altitude notée <math|h>, au dessus d'une Terre de rayon
  <math|r>, le repère des abscisses va de l'ISS vers le centre de la Terre,
  avec son origine à l'ISS.

  La vitesse linéaire de l'ISS est notée <math|v<rsub|0>>.

  <subsection|Paramètres pertinents>

  Nous fixerons l'altitude de l'ISS à <math|400 km>, sur une orbite
  parfaitement circulaire.

  Nous supposerons la Terre parfaitement sphérique de rayon <math|r=6371 km>
  et de masse <math|M<rsub|t>=5.972 \<times\>10<rsup|24> kg>, la constante de
  gravitation est fixée à <math|G=6.6742 \<times\>10<rsup|-11>
  N\<cdot\>m<rsup|2>\<cdot\>kg<rsup|-2>.>

  <section|Défrichage>

  Dans cette partie nous allons simplifier le problème à donf. Négliger tout
  ce qui peut l'être et linéariser au rouleau-compresseur. Avec un peu de
  chance, ça suffira.

  On travaille avec une corde de section constante, de masse linéaire
  <math|m<rsub|l>>.

  <subsection|Approximations grossières>

  <\enumerate>
    <item>Pas d'atmosphère: cette approximation est raisonnable jusque vers
    <math|100 km> d'altitude, elle devient totalement fausse assez vite en se
    rapprochant du sol.

    <item>Pas d'effets autres qu'inertiels ou gravitationnels: il y a en
    particulier des effets électriques dû au potentiel de la Terre, aux
    rayonnements ionisants, etc. Aucune idée de sa limite.

    <item>Linéarisation du potentiel terrestre: la relation réelle est en
    <math|1/r<rsup|2>>, mais comme je suis une grosse faignasse (et que
    l'intégration de bidule un tant soit peu compliqué, je veux pas), on va
    linéariser. Vu que <math|400\<ll\>6300>, c'est pas déraisonnable.

    <item>Linéarisation de la force centrifuge, à plus forte raison, ça doit
    marcher.

    <item>On suppose que le poids de la corde est négligeable devant la masse
    de l'ISS, c'est un point à rediscuter en fonction des résultats. On peut
    toujours affiner la corde (si les valeurs ne deviennent pas ridicules,
    certes).

    \;
  </enumerate>

  <subsection|Calculs>

  En <math|x=0>, on a un champs gravitationnel
  <math|g<rsub|0>=GM/<around*|(|r+h|)>>, et un \S<nbsp>champs
  centrifuge<nbsp>\T <math|f<rsub|0>=-v<rsub|0><rsup|2>/<around*|(|r+h|)>=-g<rsub|0>>
  (vu qu'on est en équilibre à l'orbite, c'est une conséquence de
  l'approximation 5).

  En <math|x=h>, on a un champs gravitationnel <math|g<rsub|h>=GM/r>, et un
  champs centrifuge <math|f<rsub|h>=-v<rsub|h><rsup|2>/r>.

  <subsubsection|Vitesse linéaire>

  La vitesse angulaire étant constante, on a:
  <math|\<varpi\>=<frac|v<rsub|0>|r+h>=<frac|v<rsub|h>|r>>, donc
  <math|v<rsub|h>=<frac|r|r+h>v<rsub|0>>

  <subsubsection|Champs centrifuge en h>

  <math|f<rsub|h>=-<frac|v<rsub|h><rsup|2>|r>=-<frac|r<rsup|2>|r<around*|(|r+h|)><rsup|2>>v<rsup|2><rsub|0>=-<frac|r|r+h><frac|v<rsup|2><rsub|0<rsup|>>|r+h>=<frac|r|r+h>f<rsub|0>>

  \;

  <subsubsection|Linéarisation du champs gravitationnel>

  Trivialement, <math|g<around*|(|x|)>=g<rsub|0>+<frac|g<rsub|h>-g<rsub|0>|h>x=g<rsub|0>+\<Delta\><rsub|g>x>

  <subsubsection|Linéarisation du champs centrifuge>

  <math|f<around*|(|x|)>=f<rsub|0>+\<Delta\><rsub|f>x>, avec
  <math|\<Delta\><rsub|f>=<frac|f<rsub|h>-f<rsub|0>|h>>

  <subsubsection|Poids intégré d'un élément de corde>

  Un élément de corde pèse donc: <math|p<around*|(|x|)>dx=<around*|(|g<around*|(|x|)>+f<around*|(|x|)>|)>m<rsub|l>dx>

  <subsubsection|Traction d'un morceau de corde de longueur x à son point
  d'attache>

  <\eqnarray*>
    <tformat|<table|<row|<cell|P<around*|(|x|)>>|<cell|=>|<cell|<big|int><rsub|<rsup|>0><rsup|x>p<around*|(|x|)>dx>>|<row|<cell|>|<cell|=>|<cell|<big|int><rsub|<rsup|>0><rsup|x><around*|(|g<around*|(|x|)>+f<around*|(|x|)>|)>m<rsub|l>dx>>|<row|<cell|>|<cell|=>|<cell|<big|int><rsub|<rsup|>0><rsup|x><around*|(|g<rsub|0>+f<rsub|0>+<around*|(|\<Delta\><rsub|g>+\<Delta\><rsub|f>|)>x|)>m<rsub|l>dx>>|<row|<cell|>|<cell|=>|<cell|m<rsub|l><around*|(|<around*|(|g<rsub|0>+f<rsub|0>|)>x+<frac|\<Delta\><rsub|g>+\<Delta\><rsub|f>|2>x<rsup|2>|)>>>>>
  </eqnarray*>

  <subsection|Application numérique>

  D'après Corentin G.<\footnote>
    https://www.facebook.com/groups/709019235826352/permalink/3580498048678442/?comment_id=3580984385296475
  </footnote>, une \S<nbsp>Paracorde 550<nbsp>\T a une masse linéaire de
  <math|m<rsub|l>=7.4g/m> et résiste à 2500N de traction.

  En résolvant <math|P<around*|(|400km|)>=2426N>.

  La masse totale de corde serait de moins de 3 tonnes, à comparer aux 400T
  de l'ISS.

  Non seulement ça passe, mais en plus on dirait qu'elle a été conçue pour
  cela :-)

  <section|Conclusion (provisoire)>

  Sans atmosphère, la pêche à la mouche depuis l'ISS est envisageable. Y'a
  plus qu'à.

  (sous réserve d'énormités de calculs toujours possible, document non
  contractuel, suggestion de présentation, à utiliser sous la responsabilité
  d'un adulte qualifié, ne pas reproduire à la maison).

  \;

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
    <associate|auto-1|<tuple|1|1>>
    <associate|auto-10|<tuple|3.2.2|?>>
    <associate|auto-11|<tuple|3.2.3|?>>
    <associate|auto-12|<tuple|3.2.4|?>>
    <associate|auto-13|<tuple|3.2.5|?>>
    <associate|auto-14|<tuple|3.2.6|?>>
    <associate|auto-15|<tuple|3.3|?>>
    <associate|auto-16|<tuple|4|?>>
    <associate|auto-2|<tuple|2|1>>
    <associate|auto-3|<tuple|2.1|1>>
    <associate|auto-4|<tuple|2.2|1>>
    <associate|auto-5|<tuple|2.3|2>>
    <associate|auto-6|<tuple|3|?>>
    <associate|auto-7|<tuple|3.1|?>>
    <associate|auto-8|<tuple|3.2|?>>
    <associate|auto-9|<tuple|3.2.1|?>>
    <associate|figas11|<tuple|1|?>>
    <associate|footnote-1|<tuple|1|?>>
    <associate|footnote-2|<tuple|2|?>>
    <associate|footnote-3|<tuple|3|?>>
    <associate|footnote-4|<tuple|4|?>>
    <associate|footnr-1|<tuple|1|?>>
    <associate|footnr-2|<tuple|2|?>>
    <associate|footnr-3|<tuple|3|?>>
    <associate|footnr-4|<tuple|4|?>>
    <associate|part:code/python/fittable.tm|<tuple|2|?|space_temperature.tm>>
    <associate|part:fittable2.tm|<tuple|4|?|space_temperature.tm>>
  </collection>
</references>

<\auxiliary>
  <\collection>
    <\associate|toc>
      <vspace*|1fn><with|font-series|<quote|bold>|math-font-series|<quote|bold>|1<space|2spc>Introduction>
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-1><vspace|0.5fn>

      <vspace*|1fn><with|font-series|<quote|bold>|math-font-series|<quote|bold>|2<space|2spc>Présentation
      du problème> <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-2><vspace|0.5fn>

      <with|par-left|<quote|1tab>|2.1<space|2spc>Description
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-3>>

      <with|par-left|<quote|1tab>|2.2<space|2spc>Schéma et notations
      associées <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-4>>

      <with|par-left|<quote|1tab>|2.3<space|2spc>Paramètres pertinents
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-5>>

      <vspace*|1fn><with|font-series|<quote|bold>|math-font-series|<quote|bold>|3<space|2spc>Défrichage>
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-6><vspace|0.5fn>

      <with|par-left|<quote|1tab>|3.1<space|2spc>Approximations grossières
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-7>>

      <with|par-left|<quote|1tab>|3.2<space|2spc>
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-8>>
    </associate>
  </collection>
</auxiliary>
