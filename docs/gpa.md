# OCDS for GPA: Annotated Revised GPA

This document annotates selected parts of the GPA, with details on how to publish the information using OCDS in a way that is consistent with the rules of the GPA. It is intended for a policy audience.

```eval_rst
  .. warning::
    References from Articles VII:3, VII:4, VII:5, IX:8, IX:9, X:7, X:9, X:11, XIII:2, XIV:1, XVI:2 are not yet added.
```

<table>
  <thead>
    <tr>
      <th>GPA reference</th>
      <th>GPA text</th>
      <th>OCDS guidance</th>
    </tr>
  </thead>
  <tbody>
    <tr class="section">
      <td><a href="https://www.wto.org/english/docs_e/legal_e/rev-gpr-94_01_e.htm#articleVII">VII:2</a></td>
      <td colspan="2">Except as otherwise provided in this Agreement, each notice of intended procurement shall include:</td>
    </tr>
    <tr>
      <td>VII:2(a)</td>
      <td>the name and address of the procuring entity and other information necessary to contact the procuring entity and obtain all relevant documents relating to the procurement, and their cost and terms of payment, if any;</td>
      <td>
        <ul>
          <li>Use <code>tender/procuringEntity</code> to refer to an <code>Organization</code> entry in the <code>parties</code> array.</li>
          <li>Add 'procuringEntity' to the party's <code>roles</code>.</li>
          <li>Enter the <q>name of the procuring entity</q> in <code>tender/procuringEntity/name</code> and in the party's <code>name</code>.</li>
          <li>Enter the <q>address of the procuring entity</q> in the party's <code>address</code>.</li>
          <li>Enter <q>other information necessary to contact the procuring entity</q> in the party's <code>contactPoint</code>.</li>
          <li>You may proactiveley enter the <q>cost and terms of payment</q> of <q>all relevant documents relating to the procurement</q> in <code>tender/participationFees</code>.</li>
          <li>You may proactively enter any <q>relevant documents relating to the procurement</q> in <code>tender/documents</code>.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>VII:2(b)</td>
      <td>a description of the procurement, including the nature and the quantity of the goods or services to be procured or, where the quantity is not known, the estimated quantity;</td>
      <td>
        <ul>
          <li>Enter <q>a description of the procurement</q> in <code>tender/description</code>.</li>
          <li>Enter <q>the nature and the quantity of the goods or services to be procured or, where the quantity is not known, the estimated quantity</q> in <code>tender/description</code> or, if possible, split this into <code>Item</code> entries in the <code>tender/items</code> array; enter <q>the nature</q> in the item's <code>description</code> and/or <code>unit</code> and <q>the quantity</q> in the item's <code>quantity</code>.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>VII:2(c)</td>
      <td>for recurring contracts, an estimate, if possible, of the timing of subsequent notices of intended procurement;</td>
      <td>
        <ul>
          <li>Enter <q>an estimate, if possible, of the timing of subsequent notices of intended procurement</q> in <code>tender/recurrence/dates</code>.</li>
          <li>Enter any further information in <code>tender/recurrence/description</code>.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>VII:2(d)</td>
      <td>a description of any options;</td>
      <td>
        <ul>
          <li>Enter this in <code>tender/options</code>.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>VII:2(e)</td>
      <td>the time-frame for delivery of goods or services or the duration of the contract;</td>
      <td>
        <ul>
          <li>
            <p>Enter <q>the duration of the contract</q> in <code>tender/contractPeriod</code>, or:</p>
            <ul>
              <li>Add a <code>Milestone</code> object to the <code>tender/milestones</code> array.</li>
              <li>Use 'delivery' for the milestone's <code>type</code>.</li>
              <li>Enter <q>the time-frame for delivery of goods or services</q> in the milestone's <code>period</code> <em>or</em> <code>dueDate</code>.</li>
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
          <li>Use 'open', 'selective' or 'limited' for <q>the procurement method that will be used</q> in <code>tender/procurementMethod</code>.</li>
          <li>If <q>it will involve negotiation</q>, add 'negotiated' to <code>tender/procurementMethodModalities</code>.</li>
          <li>If <q>it will involve … electronic auction</q>, add 'electronicAuction' to <code>tender/procurementMethodModalities</code>.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>VII:2(g)</td>
      <td>where applicable, the address and any final date for the submission of requests for participation in the procurement;</td>
      <td>
        <ul>
          <li>Add a <code>Milestone</code> object to the <code>tender/milestones</code> array.</li>
          <li>Use 'requestToParticipate' for the milestone's <code>type</code>.</li>
          <li>Enter <q>any final date for the submission of requests for participation in the procurement</q> in the milestone's <code>dueDate</code>.</li>
          <li>Add <q>the address … for the submission of requests for participation in the procurement</q> to the milestone's <code>description</code>.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>VII:2(h)</td>
      <td>the address and the final date for the submission of tenders;</td>
      <td>
        <ul>
          <li>Enter <q>the final date for the submission of tenders</q> in <code>tender/tenderPeriod/endDate</code>.</li>
          <li>Add <q>the address … for the submission of tenders</q> to <code>tender/submissionMethodDetails</code>.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>VII:2(i)</td>
      <td>the language or languages in which tenders or requests for participation may be submitted, if they may be submitted in a language other than an official language of the Party of the procuring entity;</td>
      <td>
        <ul>
          <li>Enter <q>the language or languages in which tenders or requests for participation may be submitted</q> in <code>contactPoint/availableLanguage</code>, in the <code>Organization</code> entry in the <code>parties</code> array referred by <code>tender/procuringEntity</code>.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>VII:2(j)</td>
      <td>a list and brief description of any conditions for participation of suppliers, including any requirements for specific documents or certifications to be provided by suppliers in connection therewith, unless such requirements are included in tender documentation that is made available to all interested suppliers at the same time as the notice of intended procurement;</td>
      <td>
        <ul>
          <li>Add this to <code>tender/eligibilityCriteria</code>.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>VII:2(k)</td>
      <td>where, pursuant to Article IX, a procuring entity intends to select a limited number of qualified suppliers to be invited to tender, the criteria that will be used to select them and, where applicable, any limitation on the number of suppliers that will be permitted to tender; and</td>
      <td>
        <ul>
          <li>Add this to <code>tender/eligibilityCriteria</code>.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>VII:2(l)</td>
      <td>an indication that the procurement is covered by this Agreement.</td>
      <td>
        <ul>
          <li>Add 'GPA' to <code>tender/flags</code>.</li>
        </ul>
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
