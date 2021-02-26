<TeXmacs|1.99.17>

<style|<tuple|article|old-spacing|old-dots|old-lengths>>

<\body>
  <\doc-data|<doc-title|Day and night duration on
  Earth>|<doc-author|<\author-data|<author-name|TK>>
    \;
  <|author-data>
    \;
  <|author-data>
    \;
  </author-data>>>
    \;
  </doc-data>

  <section|Introduction>

  Starting from the simple explanatioon \PAs Earth globe self-rotates on
  itself in about 24h on an axis that is about 23\<degree\> from normal to
  ecliptic plane where it rotates in one year around Sun, day is when Sun can
  be seen in the sky, as on the lighted side, and night when Sun goes under
  the horizon and is hidden by Earth's mass\Q, we'll compute day and night
  duration on Earth.

  \;

  <section|Some math on a sphere>

  \;
</body>

<\initial>
  <\collection>
    <associate|global-title|Day and night duration on Earth>
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
    <associate|footnote-1|<tuple|1|?>>
    <associate|footnr-1|<tuple|1|?>>
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

      <with|par-left|<quote|1tab>|3.2<space|2spc>Calculs
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-8>>

      <with|par-left|<quote|2tab>|3.2.1<space|2spc>Vitesse linéaire
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-9>>

      <with|par-left|<quote|2tab>|3.2.2<space|2spc>Champs centrifuge en h
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-10>>

      <with|par-left|<quote|2tab>|3.2.3<space|2spc>Linéarisation du champs
      gravitationnel <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-11>>

      <with|par-left|<quote|2tab>|3.2.4<space|2spc>Linéarisation du champs
      centrifuge <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-12>>

      <with|par-left|<quote|2tab>|3.2.5<space|2spc>Poids intégré d'un élément
      de corde <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-13>>

      <with|par-left|<quote|2tab>|3.2.6<space|2spc>Traction d'un morceau de
      corde de longueur x à son point d'attache
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-14>>

      <with|par-left|<quote|1tab>|3.3<space|2spc>Application numérique
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-15>>

      <vspace*|1fn><with|font-series|<quote|bold>|math-font-series|<quote|bold>|4<space|2spc>Conclusion
      (provisoire)> <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-16><vspace|0.5fn>
    </associate>
  </collection>
</auxiliary>