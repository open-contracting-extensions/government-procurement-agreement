# Annotated Revised GPA

```eval_rst
  .. warning::
    This is prepublication, alpha guidance.
```

This document annotates selected parts of the GPA, with details on how to publish the information using OCDS in a way that is consistent with the rules of the GPA. It is intended for a policy audience.

```eval_rst
  .. warning::
    References from Articles VII:3, VII:4, VII:5, IX:8, IX:9, X:7, X:9, X:11, XIII:2, XIV:1, XVI:2 are not yet added.
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
        <td>
          <ul>
            <li>
              Add an <code>Organization</code> object to the <code>parties</code> array:
              <ul>
                <li>Add 'procuringEntity' to its <code>roles</code></li>
                <li>Enter an identifier in its <code>id</code>, which can be arbitrary as it is primarily to allow referencing from other parts of the file</li>
                <li>Enter the <q>name of the procuring entity</q> in its <code>name</code></li>
                <li>Enter the <q>address of the procuring entity</q> in its <code>address</code></li>
                <li>Enter <q>other information necessary to contact the procuring entity</q> in its <code>contactPoint</code></li>
              </ul>
            </li>
            <li>Enter the above identifier in <code>tender/procuringEntity/id</code></li>
            <li>Enter the <q>name of the procuring entity</q> in <code>tender/procuringEntity/name</code></li>
            <li>You can proactively enter the <q>cost and terms of payment</q> of <q>all relevant documents relating to the procurement</q> in <code>tender/participationFees</code></li>
            <li>You can proactively enter any <q>relevant documents relating to the procurement</q> in <code>tender/documents</code></li>
          </ul>
          This requires the <a href="https://github.com/open-contracting-extensions/ocds_participationFee_extension">Participation Fees</a> extension.
        </td>
      </tr>
      <tr>
        <td>VII:2(b)</td>
        <td>a description of the procurement, including the nature and the quantity of the goods or services to be procured or, where the quantity is not known, the estimated quantity;</td>
        <td>
          <ul>
            <li>Enter <q>a description of the procurement</q> in <code>tender/description</code></li>
            <li>
              Enter <q>the nature and the quantity of the goods or services to be procured or, where the quantity is not known, the estimated quantity</q> in <code>tender/description</code> or, if possible, split this into <code>Item</code> objects in the <code>tender/items</code> array:
              <ul>
                <li>Enter <q>the nature</q> in an item's <code>description</code> and/or <code>unit</code></li>
                <li>Enter <q>the quantity</q> in an item's <code>quantity</code></li>
              </ul>
            </li>
          </ul>
          The method of representing an estimated quantity is <a href="https://github.com/open-contracting/standard/issues/689">under discussion</a>.
        </td>
      </tr>
      <tr>
        <td>VII:2(c)</td>
        <td>for recurring contracts, an estimate, if possible, of the timing of subsequent notices of intended procurement;</td>
        <td>
          <ul>
            <li>Enter <q>an estimate, if possible, of the timing of subsequent notices of intended procurement</q> in <code>tender/recurrence/dates</code></li>
            <li>Enter any further information in <code>tender/recurrence/description</code></li>
          </ul>
          This requires the <a href="https://github.com/open-contracting-extensions/ocds_recurrence_extension">Recurring Contracts</a> extension.
        </td>
      </tr>
      <tr>
        <td>VII:2(d)</td>
        <td>a description of any options;</td>
        <td>
          <ul>
            <li>Set <code>tender/hasOptions</code> to <code>true</code>
            <li>Enter this in <code>tender/options/description</code></li>
          </ul>
          This requires the <a href="https://github.com/open-contracting-extensions/ocds_options_extension">Options</a> extension.
        </td>
      </tr>
      <tr>
        <td>VII:2(e)</td>
        <td>the time-frame for delivery of goods or services or the duration of the contract;</td>
        <td>
          <ul>
            <li>If <q>the duration of the contract</q> is disclosed, enter it in <code>tender/contractPeriod</code></li>
            <li>If <q>the time-frame for delivery of goods or services</q> is disclosed, add a <code>Milestone</code> object to the <code>tender/milestones</code> array:
              <ul>
                <li>Use 'delivery' for its <code>type</code></li>
                <li>If <q>the time-frame for delivery of goods or services</q> is a specific date, enter it in the object's <code>dueDate</code> or, if it is a time period, enter it in the object's <code>period</code></li>
              </ul>
            </li>
          </ul>
          The addition of <code>period</code> to the <code>Milestone</code> building block is <a href="https://github.com/open-contracting/standard/issues/523#issuecomment-382608504">under discussion</a>.
        </td>
      </tr>
      <tr>
        <td>VII:2(f)</td>
        <td>the procurement method that will be used and whether it will involve negotiation or electronic auction;</td>
        <td>
          <ul>
            <li>Use 'open', 'selective' or 'limited' for <q>the procurement method that will be used</q> in <code>tender/procurementMethod</code></li>
            <li>If <q>it will involve negotiation</q>, add 'negotiated' to <code>tender/procurementMethodModalities</code></li>
            <li>If <q>it will involve electronic auction</q>, add 'electronicAuction' to <code>tender/procurementMethodModalities</code></li>
          </ul>
          This requires the <a href="https://github.com/open-contracting-extensions/ocds_procurementMethodModalities_extension">Procurement Method Modalities</a> extension.
        </td>
      </tr>
      <tr>
        <td>VII:2(g)</td>
        <td>where applicable, the address and any final date for the submission of requests for participation in the procurement;</td>
        <td>
          <ul>
            <li>
              Add a <code>Milestone</code> object to the <code>tender/milestones</code> array:
              <ul>
                <li>Use 'requestToParticipate' for its <code>type</code></li>
                <li>Enter <q>any final date for the submission of requests for participation in the procurement</q> in its <code>dueDate</code></li>
                <li>Add <q>the address for the submission of requests for participation in the procurement</q> to its <code>description</code></li>
              </ul>
            </li>
          </ul>
        </td>
      </tr>
      <tr>
        <td>VII:2(h)</td>
        <td>the address and the final date for the submission of tenders;</td>
        <td>
          <ul>
            <li>Enter <q>the final date for the submission of tenders</q> in <code>tender/tenderPeriod/endDate</code></li>
            <li>Add <q>the address for the submission of tenders</q> to <code>tender/submissionMethodDetails</code></li>
          </ul>
        </td>
      </tr>
      <tr>
        <td>VII:2(i)</td>
        <td>the language or languages in which tenders or requests for participation may be submitted, if they may be submitted in a language other than an official language of the Party of the procuring entity;</td>
        <td>
          <ul>
            <li>Find the <code>Organization</code> object in the <code>parties</code> array whose <code>id</code> matches <code>tender/procuringEntity/id</code></li>
            <li>Enter <q>the language or languages in which tenders or requests for participation may be submitted</q> in its <code>contactPoint/availableLanguage</code></li>
          </ul>
          This requires the <a href="https://github.com/open-contracting-extensions/ocds_additionalContactPoints_extension">Additional Contact Points</a> extension.
        </td>
      </tr>
      <tr>
        <td>VII:2(j)</td>
        <td>a list and brief description of any conditions for participation of suppliers, including any requirements for specific documents or certifications to be provided by suppliers in connection therewith, unless such requirements are included in tender documentation that is made available to all interested suppliers at the same time as the notice of intended procurement;</td>
        <td>
          <ul>
            <li>Add this to <code>tender/eligibilityCriteria</code></li>
          </ul>
        </td>
      </tr>
      <tr>
        <td>VII:2(k)</td>
        <td>where, pursuant to Article IX, a procuring entity intends to select a limited number of qualified suppliers to be invited to tender, the criteria that will be used to select them and, where applicable, any limitation on the number of suppliers that will be permitted to tender; and</td>
        <td>
          <ul>
            <li>Add this to <code>tender/eligibilityCriteria</code></li>
          </ul>
        </td>
      </tr>
      <tr>
        <td>VII:2(l)</td>
        <td>an indication that the procurement is covered by this Agreement.</td>
        <td>
          <ul>
            <li>Add 'GPA' to <code>tender/coveredBy</code></li>
          </ul>
          This requires the <a href="https://github.com/open-contracting-extensions/ocds_coveredBy_extension">Covered By</a> extension.
        </td>
      </tr>
<!--
      <tr class="section">
        <td>VII:3</td>
        <td colspan="2">For each case of intended procurement, a procuring entity shall publish a summary notice that is readily accessible, at the same time as the publication of the notice of intended procurement, in one of the WTO languages.  The summary notice shall contain at least the following information:</td>
      </tr>
      <tr>
        <td>VII:3(a)</td>
        <td>the subject-matter of the procurement;</td>
        <td>
          <ul>
            <li></li>
          </ul>
        </td>
      </tr>
      <tr>
        <td>VII:3(b)</td>
        <td>the final date for the submission of tenders or, where applicable, any final date for the submission of requests for participation in the procurement or for inclusion on a multi-use list; and</td>
        <td>
          <ul>
            <li></li>
          </ul>
        </td>
      </tr>
      <tr>
        <td>VII:3(c)</td>
        <td>the address from which documents relating to the procurement may be requested.</td>
        <td>
          <ul>
            <li></li>
          </ul>
        </td>
      </tr>
      <tr>
        <td>VII:4</td>
        <td>Procuring entities are encouraged to publish in the appropriate paper or electronic medium listed in Appendix III as early as possible in each fiscal year a notice regarding their future procurement plans (hereinafter referred to as "notice of planned procurement"). The notice of planned procurement should include the subject-matter of the procurement and the planned date of the publication of the notice of intended procurement.</td>
        <td>
          <ul>
            <li></li>
          </ul>
        </td>
      </tr>
      <tr>
        <td>VII:5</td>
        <td>A procuring entity covered under Annex 2 or 3 may use a notice of planned procurement as a notice of intended procurement provided that the notice of planned procurement includes as much of the information referred to in paragraph 2 as is available to the entity and a statement that interested suppliers should express their interest in the procurement to the procuring entity.</td>
        <td>
          <ul>
            <li></li>
          </ul>
        </td>
      </tr>
    </tbody>
-->
  </table>

<!--
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
        <td colspan="2">A procuring entity shall make available to suppliers tender documentation that includes all information necessary to permit suppliers to prepare and submit responsive tenders. Unless already provided in the notice of intended procurement, such documentation shall include a complete description of:</td>
      </tr>
      <tr>
        <td>X:7(a)</td>
        <td>the procurement, including the nature and the quantity of the goods or services to be procured or, where the quantity is not known, the estimated quantity and any requirements to be fulfilled, including any technical specifications, conformity assessment certification, plans, drawings or instructional materials;</td>
        <td>
          <ul>
            <li></li>
          </ul>
        </td>
      </tr>
      <tr>
        <td>X:7(b)</td>
        <td>any conditions for participation of suppliers, including a list of information and documents that suppliers are required to submit in connection with the conditions for participation;</td>
        <td>
          <ul>
            <li></li>
          </ul>
        </td>
      </tr>
      <tr>
        <td>X:7(c)</td>
        <td>all evaluation criteria the entity will apply in the awarding of the contract, and, except where price is the sole criterion, the relative importance of such criteria;</td>
        <td>
          <ul>
            <li></li>
          </ul>
        </td>
      </tr>
      <tr>
        <td>X:7(d)</td>
        <td>where the procuring entity will conduct the procurement by electronic means, any authentication and encryption requirements or other requirements related to the submission of information by electronic means;</td>
        <td>
          <ul>
            <li></li>
          </ul>
        </td>
      </tr>
      <tr>
        <td>X:7(e)</td>
        <td>where the procuring entity will hold an electronic auction, the rules, including identification of the elements of the tender related to the evaluation criteria, on which the auction will be conducted;</td>
        <td>
          <ul>
            <li></li>
          </ul>
        </td>
      </tr>
      <tr>
        <td>X:7(f)</td>
        <td>where there will be a public opening of tenders, the date, time and place for the opening and, where appropriate, the persons authorized to be present;</td>
        <td>
          <ul>
            <li></li>
          </ul>
        </td>
      </tr>
      <tr>
        <td>X:7(g)</td>
        <td>any other terms or conditions, including terms of payment and any limitation on the means by which tenders may be submitted, such as whether on paper or by electronic means; and</td>
        <td>
          <ul>
            <li></li>
          </ul>
        </td>
      </tr>
      <tr>
        <td>X:7(h)</td>
        <td>any dates for the delivery of goods or the supply of services</td>
        <td>
          <ul>
            <li></li>
          </ul>
        </td>
      </tr>
      <tr>
        <td>X:9</td>
        <td>The evaluation criteria set out in the notice of intended procurement or tender documentation may include, among others, price and other cost factors, quality, technical merit, environmental characteristics and terms of delivery</td>
        <td>
          <ul>
            <li></li>
          </ul>
        </td>
      </tr>
      <tr>
        <td>X:11</td>
        <td>
          Where, prior to the award of a contract, a procuring entity modifies the criteria or requirements set out in the notice of intended procurement or tender documentation provided to participating suppliers, or amends or reissues a notice or tender documentation, it shall transmit in writing all such modifications or amended or re-issued notice or tender documentation:<br>
          (a) to all suppliers that are participating at the time of the modification, amendment or re-issuance, where such suppliers are known to the entity, and in all other cases, in the same manner as the original information was made available; and<br>
          (b) in adequate time to allow such suppliers to modify and re-submit amended tenders, as appropriate.
        </td>
        <td>
          <ul>
            <li></li>
          </ul>
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
        <td>
          <ul>
            <li></li>
          </ul>
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
        <td>
          <ul>
            <li></li>
          </ul>
        </td>
      </tr>
      <tr>
        <td>XIV:1(b)</td>
        <td>the results of any initial evaluation of the elements of its tender where the contract is to be awarded on the basis of the most advantageous tender;  and</td>
        <td>
          <ul>
            <li></li>
          </ul>
        </td>
      </tr>
      <tr>
        <td>XIV:1(c)</td>
        <td>any other relevant information relating to the conduct of the auction.</td>
        <td>
          <ul>
            <li></li>
          </ul>
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
        <td>
          <ul>
            <li></li>
          </ul>
        </td>
      </tr>
      <tr>
        <td>XVI:2(b)</td>
        <td>the name and address of the procuring entity;</td>
        <td>
          <ul>
            <li></li>
          </ul>
        </td>
      </tr>
      <tr>
        <td>XVI:2(c)</td>
        <td>the name and address of the successful supplier;</td>
        <td>
          <ul>
            <li></li>
          </ul>
        </td>
      </tr>
      <tr>
        <td>XVI:2(d)</td>
        <td>the value of the successful tender or the highest and lowest offers taken into account in the award of the contract;</td>
        <td>
          <ul>
            <li></li>
          </ul>
        </td>
      </tr>
      <tr>
        <td>XVI:2(e)</td>
        <td>the date of award; and</td>
        <td>
          <ul>
            <li></li>
          </ul>
        </td>
      </tr>
      <tr>
        <td>XVI:2(f)</td>
        <td>the type of procurement method used, and in cases where limited tendering was used in accordance with Article XIII, a description of the circumstances justifying the use of limited tendering.</td>
        <td>
          <ul>
            <li></li>
          </ul>
        </td>
      </tr>
      <tr>
        <td>XVI:4</td>
        <td>Each Party shall collect and report to the Committee statistics on its contracts covered by this Agreement.  Each report shall cover one year and be submitted within two years of the end of the reporting period, and shall contain:</td>
        <td>
          <ul>
            <li></li>
          </ul>
        </td>
      </tr>
      <tr>
        <td>XVI:4(a)</td>
        <td>for Annex 1 procuring entities:</td>
        <td>
          <ul>
            <li></li>
          </ul>
        </td>
      </tr>
      <tr>
        <td>XVI:4(a)(i)</td>
        <td>the number and total value, for all such entities, of all contracts covered by this Agreement;</td>
        <td>
          <ul>
            <li></li>
          </ul>
        </td>
      </tr>
      <tr>
        <td>XVI:4(a)(ii)</td>
        <td>the number and total value of all contracts covered by this Agreement awarded by each such entity, broken down by categories of goods and services according to an internationally recognized uniform classification system;  and</td>
        <td>
          <ul>
            <li></li>
          </ul>
        </td>
      </tr>
      <tr>
        <td>XVI:4(a)(iii)</td>
        <td>the number and total value of all contracts covered by this Agreement awarded by each such entity under limited tendering;</td>
        <td>
          <ul>
            <li></li>
          </ul>
        </td>
      </tr>
      <tr>
        <td>XVI:4(b)</td>
        <td>for Annex 2 and 3 procuring entities, the number and total value of contracts covered by this Agreement awarded by all such entities, broken down by Annex;  and</td>
        <td>
          <ul>
            <li></li>
          </ul>
        </td>
      </tr>
      <tr>
        <td>XVI:4(c)</td>
        <td>estimates for the data required under subparagraphs (a) and (b), with an explanation of the methodology used to develop the estimates, where it is not feasible to provide the data.</td>
        <td>
          <ul>
            <li></li>
          </ul>
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
        <td>
          <ul>
            <li></li>
          </ul>
        </td>
      </tr>
-->
