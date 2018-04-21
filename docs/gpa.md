# Annotated Revised GPA

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
                <li>Enter an arbitrary identifier in its <code>id</code></li>
                <li>Enter the <q>name of the procuring entity</q> in its <code>name</code></li>
                <li>Enter the <q>address of the procuring entity</q> in its <code>address</code></li>
                <li>Enter <q>other information necessary to contact the procuring entity</q> in its <code>contactPoint</code></li>
              </ul>
            </li>
            <li>Enter the above identifier in <code>tender/procuringEntity/id</code></li>
            <li>Enter the <q>name of the procuring entity</q> in <code>tender/procuringEntity/name</code></li>
            <li>You may proactively enter the <q>cost and terms of payment</q> of <q>all relevant documents relating to the procurement</q> in <code>tender/participationFees</code></li>
            <li>You may proactively enter any <q>relevant documents relating to the procurement</q> in <code>tender/documents</code></li>
          </ul>
          This requires the Participation Fees extension.
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
          </ul>
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
          This requires the Recurring Contracts extension.
        </td>
      </tr>
      <tr>
        <td>VII:2(d)</td>
        <td>a description of any options;</td>
        <td>
          <ul>
            <li>Enter this in <code>tender/options</code></li>
          </ul>
          This requires the Options extension.
        </td>
      </tr>
      <tr>
        <td>VII:2(e)</td>
        <td>the time-frame for delivery of goods or services or the duration of the contract;</td>
        <td>
          <ul>
            <li>
              Enter <q>the duration of the contract</q> in <code>tender/contractPeriod</code> and/or add a <code>Milestone</code> object to the <code>tender/milestones</code> array:
              <ul>
                <li>Use 'delivery' for its <code>type</code></li>
                <li>Enter <q>the time-frame for delivery of goods or services</q> in its <code>dueDate</code> <strong>or</strong> <code>period</code></li>
              </ul>
            </li>
          </ul>
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
          This requires the Procurement Method Modalities extension.
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
          This requires the Covered By extension.
        </td>
      </tr>
      <!--
      <tr>
        <td></td>
        <td></td>
        <td>
          
        </td>
      </tr>
      -->
    </tbody>
  </table>
</div>
