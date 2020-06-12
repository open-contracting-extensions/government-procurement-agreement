# Annotated Revised GPA

```eval_rst
.. warning::

   This is prepublication, alpha guidance.
```

This document annotates selected parts of the GPA, with details on how to publish the information using OCDS in a way that is consistent with the rules of the GPA. It is intended for a policy audience.

```eval_rst
.. warning::

   References from Articles VII:4, VII:5, IX:8, IX:9, X:7, X:9, X:11, XIII:2, XIV:1, XVI:2 are not yet added.
```

<div class="wy-table-responsive">
  <table class="docutils">
    <caption><a href="https://www.wto.org/english/docs_e/legal_e/rev-gpr-94_01_e.htm#articleVII">Article VII</a> Notices</caption>
    <colgroup>
      <col width="10%">
      <col width="40%">
      <col width="50%">
    </colgroup>
    <thead>
      <tr>
        <th>Reference</th>
        <th>GPA text</th>
        <th>OCDS guidance</th>
      </tr>
    </thead>
    <tbody>
      <tr class="section">
        <td>VII:2</td>
        <td colspan="2">Except as otherwise provided in this Agreement, each notice of intended procurement shall include:</td>
      </tr>
      <tr>
        <td>VII:2(a)</td>
        <td>the name and address of the procuring entity and other information necessary to contact the procuring entity and obtain all relevant documents relating to the procurement, and their cost and terms of payment, if any;</td>
        <td markdown=1>

* Add an `Organization` object to the `parties` array:
    * Add 'procuringEntity' to its `roles`
    * Enter an identifier in its `id`, which can be arbitrary as it is primarily to allow referencing from other parts of the file
    * Enter the *name of the procuring entity* in its `name`
    * Enter the *address of the procuring entity* in its `address`
    * Enter *other information necessary to contact the procuring entity* in its `contactPoint`
* Enter the above identifier in `tender/procuringEntity/id`
* Enter the *name of the procuring entity* in `tender/procuringEntity/name`
* You can proactively enter the *cost and terms of payment* of *all relevant documents relating to the procurement* in `tender/participationFees`
* You can proactively enter any *relevant documents relating to the procurement* in `tender/documents`

This requires the [Participation Fees](https://github.com/open-contracting-extensions/ocds_participationFee_extension) extension.
</td>
      </tr>
      <tr>
        <td>VII:2(b)</td>
        <td>a description of the procurement, including the nature and the quantity of the goods or services to be procured or, where the quantity is not known, the estimated quantity;</td>
        <td markdown=1>

* Enter *a description of the procurement* in `tender/description`
* Enter *the nature and the quantity of the goods or services to be procured or, where the quantity is not known, the estimated quantity* in `tender/description` or, if possible, split this into `Item` objects in the `tender/items` array:
    * Enter *the nature* in an item's `description` and/or `unit`
    * Enter *the quantity* in an item's `quantity`

The method of representing an estimated quantity is [under discussion](https://github.com/open-contracting/standard/issues/689).
</td>
      </tr>
      <tr>
        <td>VII:2(c)</td>
        <td>for recurring contracts, an estimate, if possible, of the timing of subsequent notices of intended procurement;</td>
        <td markdown=1>

* Set `tender/hasRecurrence` to `true`
* Enter *an estimate, if possible, of the timing of subsequent notices of intended procurement* in `tender/recurrence/dates`
* Enter any further information in `tender/recurrence/description`

This requires the [Recurrence](https://github.com/open-contracting-extensions/ocds_recurrence_extension) extension.
</td>
      </tr>
      <tr>
        <td>VII:2(d)</td>
        <td>a description of any options;</td>
        <td markdown=1>

* Set `tender/hasOptions` to `true`
* Enter this in `tender/options/description`

This requires the [Options](https://github.com/open-contracting-extensions/ocds_options_extension) extension.
</td>
      </tr>
      <tr>
        <td>VII:2(e)</td>
        <td>the time-frame for delivery of goods or services or the duration of the contract;</td>
        <td markdown=1>

* If *the duration of the contract* is disclosed, enter it in `tender/contractPeriod`
* If *the time-frame for delivery of goods or services* is disclosed, add a `Milestone` object to the `tender/milestones` array:
    * Use 'delivery' for its `type`
    * If *the time-frame for delivery of goods or services* is a specific date, enter it in the object's `dueDate` or, if it is a time period, enter it in the object's `period`

The addition of `period` to the `Milestone` building block is [under discussion](https://github.com/open-contracting/standard/issues/523#issuecomment-382608504).
</td>
      </tr>
      <tr>
        <td>VII:2(f)</td>
        <td>the procurement method that will be used and whether it will involve negotiation or electronic auction;</td>
        <td markdown=1>

* Use 'open', 'selective' or 'limited' for *the procurement method that will be used* in `tender/procurementMethod`
* If *it will involve negotiation*, add "negotiated" to `tender/procurementMethodDetails`
* If *it will involve electronic auction* set `tender/techniques/hasElectronicAuction` to `true`

This requires the [Techniques](https://github.com/open-contracting-extensions/ocds_techniques_extension) extension.
</td>
      </tr>
      <tr>
        <td>VII:2(g)</td>
        <td>where applicable, the address and any final date for the submission of requests for participation in the procurement;</td>
        <td markdown=1>

* Add a `Milestone` object to the `tender/milestones` array:
    * Use 'requestToParticipate' for its `type`
    * Enter *any final date for the submission of requests for participation in the procurement* in its `dueDate`
    * Add *the address for the submission of requests for participation in the procurement* to its `description`
</td>
      </tr>
      <tr>
        <td>VII:2(h)</td>
        <td>the address and the final date for the submission of tenders;</td>
        <td markdown=1>

* Enter *the final date for the submission of tenders* in `tender/tenderPeriod/endDate`
* Add *the address for the submission of tenders* to `tender/submissionMethodDetails`
</td>
      </tr>
      <tr>
        <td>VII:2(i)</td>
        <td>the language or languages in which tenders or requests for participation may be submitted, if they may be submitted in a language other than an official language of the Party of the procuring entity;</td>
        <td markdown=1>

* Find the `Organization` object in the `parties` array whose `id` matches `tender/procuringEntity/id`
* Enter *the language or languages in which tenders or requests for participation may be submitted* in its `contactPoint/availableLanguage`

This requires the [Additional Contact Points](https://github.com/open-contracting-extensions/ocds_additionalContactPoints_extension) extension.
</td>
      </tr>
      <tr>
        <td>VII:2(j)</td>
        <td>a list and brief description of any conditions for participation of suppliers, including any requirements for specific documents or certifications to be provided by suppliers in connection therewith, unless such requirements are included in tender documentation that is made available to all interested suppliers at the same time as the notice of intended procurement;</td>
        <td markdown=1>

* Add this to `tender/eligibilityCriteria`
</td>
      </tr>
      <tr>
        <td>VII:2(k)</td>
        <td>where, pursuant to Article IX, a procuring entity intends to select a limited number of qualified suppliers to be invited to tender, the criteria that will be used to select them and, where applicable, any limitation on the number of suppliers that will be permitted to tender; and</td>
        <td markdown=1>

* Enter *the number of suppliers that will be permitted to tender* in `tender.secondStage.maximumCandidates`

This requires the [Second Stage](https://github.com/open-contracting-extensions/ocds_secondStage_extension) extension.

* Add *the criteria that will be used to select [the suppliers]* to `tender.selectionCriteria.description` or, if possible, split this into `SelectionCriterion` objects in the `tender/selectionCriteria/criteria` array.

This requires the [Selection Criteria](https://github.com/open-contracting-extensions/ocds_selectionCriteria_extension) extension.
</td>
      </tr>
      <tr>
        <td>VII:2(l)</td>
        <td>an indication that the procurement is covered by this Agreement.</td>
        <td markdown=1>

* Add 'GPA' to `tender/coveredBy`

This requires the [Covered By](https://github.com/open-contracting-extensions/ocds_coveredBy_extension) extension.
</td>
      </tr>
      <tr class="section">
        <td>VII:3</td>
        <td colspan="2">For each case of intended procurement, a procuring entity shall publish a summary notice that is readily accessible, at the same time as the publication of the notice of intended procurement, in one of the WTO languages.  The summary notice shall contain at least the following information:</td>
      </tr>
      <tr>
        <td>VII:3(a)<br/>
        VII:3(b)<br/>
        VII:3(c)<br/></td>
        <td>the subject-matter of the procurement;<br/>
        the final date for the submission of tenders or, where applicable, any final date for the submission of requests for participation in the procurement or for inclusion on a multi-use list; and<br/>
        the address from which documents relating to the procurement may be requested.</td>
        <td markdown=1>

The information included in the notice of intended procurement covers all the information included in a summary notice. As such, no OCDS release needs to be published that corresponds to the summary notice.

</td>
      </tr>
      <tr>
        <td>VII:4</td>
        <td>Procuring entities are encouraged to publish in the appropriate paper or electronic medium listed in Appendix III as early as possible in each fiscal year a notice regarding their future procurement plans (hereinafter referred to as "notice of planned procurement"). The notice of planned procurement should include the subject-matter of the procurement and the planned date of the publication of the notice of intended procurement.</td>
        <td markdown=1>

* Enter *the subject-matter of the procurement* in `planning/rationale`
* Enter *the planned date of the publication of the notice of intended procurement* in `tender/tenderPeriod/startDate`
</td>
      </tr>
      <tr>
        <td>VII:5</td>
        <td>A procuring entity covered under Annex 2 or 3 may use a notice of planned procurement as a notice of intended procurement provided that the notice of planned procurement includes as much of the information referred to in paragraph 2 as is available to the entity and a statement that interested suppliers should express their interest in the procurement to the procuring entity.</td>
        <td markdown=1>

* If at the time of publishing a notice of planned procurement (article VII:4) you have all the necessary information to publish a notice of intended procurement (VII:2), follow the guidance for article VII:2, instead of the guidance for article VII:4.
</td>
      </tr>
    </tbody>
  </table>

  <table class="docutils">
    <caption><a href="https://www.wto.org/english/docs_e/legal_e/rev-gpr-94_01_e.htm#articleX">Article X</a> Notices</caption>
    <colgroup>
      <col width="10%">
      <col width="40%">
      <col width="50%">
    </colgroup>
    <thead>
      <tr>
        <th>Reference</th>
        <th>GPA text</th>
        <th>OCDS guidance</th>
      </tr>
    </thead>
    <tbody>
      <tr class="section">
        <td>X:7</td>
        <td>A procuring entity shall make available to suppliers tender documentation that includes all information necessary to permit suppliers to prepare and submit responsive tenders. Unless already provided in the notice of intended procurement, such documentation shall include a complete description of:</td>
        <td markdown=1>

* If at the time of publishing tender documentation (article X:7) you have already published all the information necessary for a notice of intended procurement (article VII:2), and this information has not changed, discard this article.
* If you haven't published all the information necessary for a notice of intended procurement or if the information has changed, follow the guidance for article VII:2 to publish the new and updated data.
        </td>
      </tr>
      <tr>
        <td>X:9</td>
        <td>The evaluation criteria set out in the notice of intended procurement or tender documentation may include, among others, price and other cost factors, quality, technical merit, environmental characteristics and terms of delivery</td>
        <td markdown=1>

* Enter the *evaluation criteria set out in the notice of intended procurement or tender documentation* in `tender/awardCriteria/description`, or, if possible, split this into `AwardCriterion` objects in the `tender/awardCriteria/criteria` array.

This requires the [Award Criteria](https://github.com/open-contracting-extensions/ocds_awardCriteria_extension) extension.


</td>
      </tr>
      <tr>
        <td>X:11</td>
        <td markdown=1>
          Where, prior to the award of a contract, a procuring entity modifies the criteria or requirements set out in the notice of intended procurement or tender documentation provided to participating suppliers, or amends or reissues a notice or tender documentation, it shall transmit in writing all such modifications or amended or re-issued notice or tender documentation:<br>
          (a) to all suppliers that are participating at the time of the modification, amendment or re-issuance, where such suppliers are known to the entity, and in all other cases, in the same manner as the original information was made available; and<br>
          (b) in adequate time to allow such suppliers to modify and re-submit amended tenders, as appropriate.
</td>
        <td markdown=1>

* Create a new OCDS release and follow the corresponding guidance, depending on the information that has been modified:
  * If the *the criteria or requirements* are modified, follow the guidance for article X:9
  * If *a notice* (of intended procurement) is amended or reissued, follow the guidance of article VII:2
  * If the *tender documentation* is amended or reissued, follow the guidance for article X:7

</td>
      </tr>
    </tbody>
  </table>

  <table class="docutils">
    <caption><a href="https://www.wto.org/english/docs_e/legal_e/rev-gpr-94_01_e.htm#articleXIII">Article XIII</a> Notices</caption>
    <colgroup>
      <col width="10%">
      <col width="40%">
      <col width="50%">
    </colgroup>
    <thead>
      <tr>
        <th>Reference</th>
        <th>GPA text</th>
        <th>OCDS guidance</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>XIII:2</td>
        <td>A procuring entity shall prepare a report in writing on each contract awarded under paragraph 1. The report shall include the name of the procuring entity, the value and kind of goods or services procured and a statement indicating the circumstances and conditions described in paragraph 1 that justified the use of limited tendering.</td>
        <td markdown=1>

* 
</td>
      </tr>
    </tbody>
  </table>

  <table class="docutils">
    <caption><a href="https://www.wto.org/english/docs_e/legal_e/rev-gpr-94_01_e.htm#articleXIV">Article XIV</a> Notices</caption>
    <colgroup>
      <col width="10%">
      <col width="40%">
      <col width="50%">
    </colgroup>
    <thead>
      <tr>
        <th>Reference</th>
        <th>GPA text</th>
        <th>OCDS guidance</th>
      </tr>
    </thead>
    <tbody>
      <tr class="section">
        <td>XIV:1</td>
        <td colspan="2">Where a procuring entity intends to conduct a covered procurement using an electronic auction, the entity shall provide each participant, before commencing the electronic auction, with:</td>
      </tr>
      <tr>
        <td>XIV:1(a)</td>
        <td>the automatic evaluation method, including the mathematical formula, that is based on the evaluation criteria set out in the tender documentation and that will be used in the automatic ranking or re-ranking during the auction;</td>
        <td markdown=1>

* 
</td>
      </tr>
      <tr>
        <td>XIV:1(b)</td>
        <td>the results of any initial evaluation of the elements of its tender where the contract is to be awarded on the basis of the most advantageous tender;  and</td>
        <td markdown=1>

* 
</td>
      </tr>
      <tr>
        <td>XIV:1(c)</td>
        <td>any other relevant information relating to the conduct of the auction.</td>
        <td markdown=1>

* 
</td>
      </tr>
    </tbody>
  </table>

  <table class="docutils">
    <caption><a href="https://www.wto.org/english/docs_e/legal_e/rev-gpr-94_01_e.htm#articleXVI">Article XVI</a> Notices</caption>
    <colgroup>
      <col width="10%">
      <col width="40%">
      <col width="50%">
    </colgroup>
    <thead>
      <tr>
        <th>Reference</th>
        <th>GPA text</th>
        <th>OCDS guidance</th>
      </tr>
    </thead>
    <tbody>
      <tr class="section">
        <td>XVI:2</td>
        <td colspan="2">Not later than 72 days after the award of each contract covered by this Agreement, a procuring entity shall publish a notice in the appropriate paper or electronic medium listed in Appendix III. Where the entity publishes the notice only in an electronic medium, the information shall remain readily accessible for a reasonable period of time. The notice shall include at least the following information:</td>
      </tr>
      <tr>
        <td>XVI:2(a)</td>
        <td>a description of the goods or services procured;</td>
        <td markdown=1>

* 
</td>
      </tr>
      <tr>
        <td>XVI:2(b)</td>
        <td>the name and address of the procuring entity;</td>
        <td markdown=1>

* 
</td>
      </tr>
      <tr>
        <td>XVI:2(c)</td>
        <td>the name and address of the successful supplier;</td>
        <td markdown=1>

* 
</td>
      </tr>
      <tr>
        <td>XVI:2(d)</td>
        <td>the value of the successful tender or the highest and lowest offers taken into account in the award of the contract;</td>
        <td markdown=1>

* 
</td>
      </tr>
      <tr>
        <td>XVI:2(e)</td>
        <td>the date of award; and</td>
        <td markdown=1>

* 
</td>
      </tr>
      <tr>
        <td>XVI:2(f)</td>
        <td>the type of procurement method used, and in cases where limited tendering was used in accordance with Article XIII, a description of the circumstances justifying the use of limited tendering.</td>
        <td markdown=1>

* 
</td>
      </tr>
      <tr>
        <td>XVI:4</td>
        <td>Each Party shall collect and report to the Committee statistics on its contracts covered by this Agreement.  Each report shall cover one year and be submitted within two years of the end of the reporting period, and shall contain:</td>
        <td markdown=1>

* 
</td>
      </tr>
      <tr>
        <td>XVI:4(a)</td>
        <td>for Annex 1 procuring entities:</td>
        <td markdown=1>

* 
</td>
      </tr>
      <tr>
        <td>XVI:4(a)(i)</td>
        <td>the number and total value, for all such entities, of all contracts covered by this Agreement;</td>
        <td markdown=1>

* 
</td>
      </tr>
      <tr>
        <td>XVI:4(a)(ii)</td>
        <td>the number and total value of all contracts covered by this Agreement awarded by each such entity, broken down by categories of goods and services according to an internationally recognized uniform classification system;  and</td>
        <td markdown=1>

* 
</td>
      </tr>
      <tr>
        <td>XVI:4(a)(iii)</td>
        <td>the number and total value of all contracts covered by this Agreement awarded by each such entity under limited tendering;</td>
        <td markdown=1>

* 
</td>
      </tr>
      <tr>
        <td>XVI:4(b)</td>
        <td>for Annex 2 and 3 procuring entities, the number and total value of contracts covered by this Agreement awarded by all such entities, broken down by Annex;  and</td>
        <td markdown=1>

* 
</td>
      </tr>
      <tr>
        <td>XVI:4(c)</td>
        <td>estimates for the data required under subparagraphs (a) and (b), with an explanation of the methodology used to develop the estimates, where it is not feasible to provide the data.</td>
        <td markdown=1>

* 
</td>
      </tr>
    </tbody>
  </table>
-->
</div>

<!--
      <tr class="section">
        <td></td>
        <td colspan="2"></td>
      </tr>
      <tr>
        <td></td>
        <td></td>
        <td markdown=1>

* 
</td>
      </tr>
-->
