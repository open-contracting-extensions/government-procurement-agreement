# Annotated Revised GPA

This document annotates selected parts of the GPA, with details on how to publish the information using OCDS in a way that is consistent with the rules of the GPA. It is intended for both policy and technical audiences.

## [Article VII](https://www.wto.org/english/docs_e/legal_e/rev-gpr-94_01_e.htm#articleVII) Notices

### Notice of Intended Procurement

<div class="wy-table-responsive">
  <table class="docutils">
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
      <tr id="VII:2">
        <td>VII:2</td>
        <td>Except as otherwise provided in this Agreement, each notice of intended procurement shall include:</td>
        <td markdown=1>

1. [Create an OCDS release](../operations/#create-a-release)
1. Add 'tender' to the `tag` array
1. Set `tender/status` to 'active'

</td>
      </tr>
      <tr id="VII:2(a)">
        <td>VII:2(a)</td>
        <td>the name and address of the procuring entity and other information necessary to contact the procuring entity and obtain all relevant documents relating to the procurement, and their cost and terms of payment, if any;</td>
        <td markdown=1>

1. Add an `Organization` object to the `parties` array:
    1. Add 'procuringEntity' to its `roles`
    1. Enter an identifier in its `id`, which can be arbitrary as it is primarily to allow referencing from other parts of the file
    1. Enter the *name of the procuring entity* in its `name`
    1. Enter the *address of the procuring entity* in its `address`
    1. Enter *other information necessary to contact the procuring entity* in its `contactPoint`
    1. Add a `Classification` object to its `details/classifications` array
        1. Set its `scheme` to 'gpaCoverageSchedule' ([GPA coverage schedule documentation](https://www.wto.org/english/tratop_e/gproc_e/gp_app_agree_e.htm#revisedGPA))
        1. Set its `id`
            * to 'annex1' if the procuring entity is a central government entity
            * to 'annex2' if the procuring entity a sub-central government entity
            * to 'annex3' if the procuring entity is another type of entity
1. Enter the above identifier in `tender/procuringEntity/id`
1. Enter the *name of the procuring entity* in `tender/procuringEntity/name`
1. You can proactively enter the *cost and terms of payment* of *all relevant documents relating to the procurement* in `tender/participationFees`
1. You can proactively enter any *relevant documents relating to the procurement* in `tender/documents`

This requires the [Organization Classification](https://extensions.open-contracting.org/en/extensions/organizationClassification/master/) and [Participation Fees](https://github.com/open-contracting-extensions/ocds_participationFee_extension) extensions.

</td>
      </tr>
      <tr id="VII:2(b)">
        <td>VII:2(b)</td>
        <td>a description of the procurement, including the nature and the quantity of the goods or services to be procured or, where the quantity is not known, the estimated quantity;</td>
        <td markdown=1>

1. Enter *a description of the procurement* in `tender/description`
1. Enter *the nature and the quantity of the goods or services to be procured or, where the quantity is not known, the estimated quantity* in `tender/description` or, if possible, split this into `Item` objects in the `tender/items` array:
    1. Enter *the nature* in an item's `description` and/or `unit`
    1. Enter *the quantity* in an item's `quantity`

The method of representing an estimated quantity is [under discussion](https://github.com/open-contracting/standard/issues/689).

</td>
      </tr>
      <tr id="VII:2(c)">
        <td>VII:2(c)</td>
        <td>for recurring contracts, an estimate, if possible, of the timing of subsequent notices of intended procurement;</td>
        <td markdown=1>

1. Set `tender/hasRecurrence` to `true`
1. Enter *an estimate, if possible, of the timing of subsequent notices of intended procurement* in `tender/recurrence/dates`
1. Enter any further information in `tender/recurrence/description`

This requires the [Recurrence](https://github.com/open-contracting-extensions/ocds_recurrence_extension) extension.

</td>
      </tr>
      <tr id="VII:2(d)">
        <td>VII:2(d)</td>
        <td>a description of any options;</td>
        <td markdown=1>

1. Set `tender/hasOptions` to `true`
1. Enter this in `tender/options/description`

This requires the [Options](https://github.com/open-contracting-extensions/ocds_options_extension) extension.

</td>
      </tr>
      <tr id="VII:2(e)">
        <td>VII:2(e)</td>
        <td>the time-frame for delivery of goods or services or the duration of the contract;</td>
        <td markdown=1>

1. If *the duration of the contract* is disclosed, enter it in `tender/contractPeriod`
1. If *the time-frame for delivery of goods or services* is disclosed, add a `Milestone` object to the `tender/milestones` array:
    1. Use 'delivery' for its `type`
    1. If *the time-frame for delivery of goods or services* is a specific date, enter it in the object's `dueDate` or, if it is a time period, enter it in the object's `period`

The addition of `period` to the `Milestone` building block is [under discussion](https://github.com/open-contracting/standard/issues/523#issuecomment-382608504).

</td>
      </tr>
      <tr id="VII:2(f)">
        <td>VII:2(f)</td>
        <td>the procurement method that will be used and whether it will involve negotiation or electronic auction;</td>
        <td markdown=1>

1. Use 'open', 'selective' or 'limited' for *the procurement method that will be used* in `tender/procurementMethod`
1. If *it will involve negotiation*, add "negotiated" to `tender/procurementMethodDetails`
1. If *it will involve electronic auction*, set `tender/techniques/hasElectronicAuction` to `true`

This requires the [Techniques](https://github.com/open-contracting-extensions/ocds_techniques_extension) extension.

</td>
      </tr>
      <tr id="VII:2(g)">
        <td>VII:2(g)</td>
        <td>where applicable, the address and any final date for the submission of requests for participation in the procurement;</td>
        <td markdown=1>

1. Add a `Milestone` object to the `tender/milestones` array:
    1. Use 'requestToParticipate' for its `type`
    1. Enter *any final date for the submission of requests for participation in the procurement* in its `dueDate`
    1. Add *the address for the submission of requests for participation in the procurement* to its `description`

</td>
      </tr>
      <tr id="VII:2(h)">
        <td>VII:2(h)</td>
        <td>the address and the final date for the submission of tenders;</td>
        <td markdown=1>

1. Enter *the final date for the submission of tenders* in `tender/tenderPeriod/endDate`
1. Add *the address for the submission of tenders* to `tender/submissionMethodDetails`

</td>
      </tr>
      <tr id="VII:2(i)">
        <td>VII:2(i)</td>
        <td>the language or languages in which tenders or requests for participation may be submitted, if they may be submitted in a language other than an official language of the Party of the procuring entity;</td>
        <td markdown=1>

1. Find the `Organization` object in the `parties` array whose `id` matches `tender/procuringEntity/id`
1. Enter *the language or languages in which tenders or requests for participation may be submitted* in its `contactPoint/availableLanguage`

This requires the [Additional Contact Points](https://github.com/open-contracting-extensions/ocds_additionalContactPoints_extension) extension.

</td>
      </tr>
      <tr id="VII:2(j)">
        <td>VII:2(j)</td>
        <td>a list and brief description of any conditions for participation of suppliers, including any requirements for specific documents or certifications to be provided by suppliers in connection therewith, unless such requirements are included in tender documentation that is made available to all interested suppliers at the same time as the notice of intended procurement;</td>
        <td markdown=1>

1. Add *a list and brief description of any conditions for participation of suppliers* to `tender/eligibilityCriteria`
1. If *requirements are included in tender documentation that is made available to all interested suppliers*:
    1. For each document, add a `Document` object to the `tender/documents` array
    1. Set its `documentType` to 'eligibilityCriteria'
    1. Fill any other known information for the document ([`Document` object schema](https://standard.open-contracting.org/1.1/en/schema/reference/#document))

</td>
      </tr>
      <tr id="VII:2(k)">
        <td>VII:2(k)</td>
        <td>where, pursuant to Article IX, a procuring entity intends to select a limited number of qualified suppliers to be invited to tender, the criteria that will be used to select them and, where applicable, any limitation on the number of suppliers that will be permitted to tender; and</td>
        <td markdown=1>

1. Enter *the number of suppliers that will be permitted to tender* in `tender.secondStage.maximumCandidates`
1. Add *the criteria that will be used to select [the suppliers]* to `tender.selectionCriteria.description` or, if possible, split this into `SelectionCriterion` objects in the `tender/selectionCriteria/criteria` array.
1. If *the criteria that will be used to select [the suppliers]* are published as documents:
    1. For each document, add a `Document` object to the `tender/documents` array
    1. Set its `documentType` to 'selectionCriteria'
    1. Fill any other known information for the document ([`Document` object schema](https://standard.open-contracting.org/1.1/en/schema/reference/#document))

This requires the [Second Stage Description](https://github.com/open-contracting-extensions/ocds_secondStageDescription_extension) and [Selection Criteria](https://github.com/open-contracting-extensions/ocds_selectionCriteria_extension) extensions.

</td>
      </tr>
      <tr id="VII:2(l)">
        <td>VII:2(l)</td>
        <td>an indication that the procurement is covered by this Agreement.</td>
        <td markdown=1>

1. Add 'GPA' to `tender/coveredBy`

This requires the [Covered By](https://github.com/open-contracting-extensions/ocds_coveredBy_extension) extension.

</td>
      </tr>
    </tbody>
  </table>
</div>

### Summary Notice

<div class="wy-table-responsive">
  <table class="docutils">
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
      <tr id="VII:3">
        <td>VII:3</td>
        <td colspan="2">For each case of intended procurement, a procuring entity shall publish a summary notice that is readily accessible, at the same time as the publication of the notice of intended procurement, in one of the WTO languages.  The summary notice shall contain at least the following information:</td>
      </tr>
      <tr id="VII:3(a)">
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
    </tbody>
  </table>
</div>

### Notice of Planned Procurement

<div class="wy-table-responsive">
  <table class="docutils">
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
      <tr id="VII:4">
        <td>VII:4</td>
        <td>Procuring entities are encouraged to publish in the appropriate paper or electronic medium listed in Appendix III as early as possible in each fiscal year a notice regarding their future procurement plans (hereinafter referred to as "notice of planned procurement"). The notice of planned procurement should include the subject-matter of the procurement and the planned date of the publication of the notice of intended procurement.</td>
        <td markdown=1>

1. [Create an OCDS release](../operations/#create-a-release)
1. Add 'planning' to the `tag` array
1. Set `tender/status` to 'planning'
1. Enter *the subject-matter of the procurement* in `tender/description`. The value of `tender/description` can be updated when the data described in article VII:2(b) is published.
1. Enter *the planned date of the publication of the notice of intended procurement* in `tender/communication/futureNoticeDate`
1. If *notice regarding their future procurement plans* is also published as a document:
    1. Add a `Document` object to the `tender/documents` array
    1. Set its `documentType` to 'plannedProcurementNotice'
    1. Fill any other known information for the document ([`Document` object schema](https://standard.open-contracting.org/1.1/en/schema/reference/#document))

This requires the [Communication](https://github.com/open-contracting-extensions/ocds_communication_extension) extension.

</td>
      </tr>
      <tr id="VII:5">
        <td>VII:5</td>
        <td>A procuring entity covered under Annex 2 or 3 may use a notice of planned procurement as a notice of intended procurement provided that the notice of planned procurement includes as much of the information referred to in paragraph 2 as is available to the entity and a statement that interested suppliers should express their interest in the procurement to the procuring entity.</td>
        <td markdown=1>

1. Follow the guidance for [VII:2](#VII:2).

</td>
      </tr>
    </tbody>
  </table>
</div>

## [Article IX](https://www.wto.org/english/docs_e/legal_e/rev-gpr-94_01_e.htm#articleIX) Qualification of suppliers

### Multi-Use Lists

<div class="wy-table-responsive">
  <table class="docutils">
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
      <tr id="IX:8">
        <td>IX:8</td>
        <td>The notice provided for in paragraph 7 shall include:</td>
        <td rowspan="9" markdown=1>

If you are interested in using OCDS to publish this, please contact <data@open-contracting.org> or comment on this [GitHub issue](https://github.com/open-contracting-extensions/government-procurement-agreement/issues/22).

</td>
      </tr>
      <tr id="IX:8(a)">
        <td>IX:8(a)</td>
        <td>a description of the goods or services, or categories thereof, for which the list may be used;</td>
      </tr>
      <tr id="IX:8(b)">
        <td>IX:8(b)</td>
        <td>the conditions for participation to be satisfied by suppliers for inclusion on the list and the methods that the procuring entity will use to verify that a supplier satisfies the conditions;</td>
      </tr>
      <tr id="IX:8(c)">
        <td>IX:8(c)</td>
        <td>the name and address of the procuring entity and other information necessary to contact the entity and obtain all relevant documents relating to the list;</td>
      </tr>
      <tr id="IX:8(d)">
        <td>IX:8(d)</td>
        <td>the period of validity of the list and the means for its renewal or termination, or where the period of validity is not provided, an indication of the method by which notice will be given of the termination of use of the list;  and</td>
      </tr>
      <tr id="IX:8(e)">
        <td>IX:8(e)</td>
        <td>an indication that the list may be used for procurement covered by this Agreement.</td>
      </tr>
      <tr id="IX:9">
        <td>IX:9</td>
        <td>Notwithstanding paragraph 7, where a multi-use list will be valid for three years or less, a procuring entity may publish the notice referred to in paragraph 7 only once, at the beginning of the period of validity of the list, provided that the notice:</td>
      </tr>
      <tr id="IX:9(a)">
        <td>IX:9(a)</td>
        <td>states the period of validity and that further notices will not be published;  and</td>
      </tr>
      <tr id="IX:9(b)">
        <td>IX:9(b)</td>
        <td>is published by electronic means and is made available continuously during the period of its validity.</td>
      </tr>
   </tbody>
  </table>
</div>

## [Article X](https://www.wto.org/english/docs_e/legal_e/rev-gpr-94_01_e.htm#articleX) Technical Specifications and Tender Documentation

### Tender Documentation

<div class="wy-table-responsive">
  <table class="docutils">
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
      <tr id="X:7">
        <td>X:7</td>
        <td>A procuring entity shall make available to suppliers tender documentation that includes all information necessary to permit suppliers to prepare and submit responsive tenders. Unless already provided in the notice of intended procurement, such documentation shall include a complete description of:</td>
        <td markdown=1>

1. [Create an OCDS release](../operations/#create-a-release)
1. Add 'tenderUpdate' to the `tag` array

</td>
     </tr>
      <tr id="X:7(a)">
        <td>X:7(a)</td>
        <td>the procurement, including the nature and the quantity of the goods or services to be procured or, where the quantity is not known, the estimated quantity and any requirements to be fulfilled, including any technical specifications, conformity assessment certification, plans, drawings or instructional materials;</td>
        <td markdown=1>

1. For *the procurement, including the nature and the quantity of the goods or services to be procured or, where the quantity is not known, the estimated quantity*, follow the guidance for [VII:2(b)](#VII:2(b))
1. For *any requirements to be fulfilled, including any technical specifications, conformity assessment certification, plans, drawings or instructional materials*, append to `tender/description`.

</td>
      </tr>
      <tr id="X:7(b)">
        <td>X:7(b)</td>
        <td>any conditions for participation of suppliers, including a list of information and documents that suppliers are required to submit in connection with the conditions for participation;</td>
        <td markdown=1>

1. Follow the guidance for [VII:2(j)](#VII:2(j))

</td>
      </tr>
      <tr id="X:7(c)">
        <td>X:7(c)</td>
        <td>all evaluation criteria the entity will apply in the awarding of the contract, and, except where price is the sole criterion, the relative importance of such criteria;</td>
        <td markdown=1>

1. Map *all evaluation criteria the entity will apply in the awarding of the contract* and *the relative importance of such criteria* to `tender.awardCriteriaDetails`
1. If *price is the sole criterion*, set `tender.awardCriteria` to 'priceOnly'

</td>
      </tr>
      <tr id="X:7(d)">
        <td>X:7(d)</td>
        <td>where the procuring entity will conduct the procurement by electronic means, any authentication and encryption requirements or other requirements related to the submission of information by electronic means;</td>
        <td markdown=1>

1. Set `tender/submissionMethod` to 'electronicSubmission'
1. Enter or append *authentication and encryption requirements or other requirements related to the submission of information by electronic means* in `tender/submissionMethodDetails`
1. If the electronic communication with the procuring entity requires the use of tools and devices that are not generally available, enter the Web address of these tools in `tender.communication.atypicalToolUrl`

This requires the [Communication](https://github.com/open-contracting-extensions/ocds_communication_extension) extension.

</td>
      </tr>
      <tr id="X:7(e)">
        <td>X:7(e)</td>
        <td>where the procuring entity will hold an electronic auction, the rules, including identification of the elements of the tender related to the evaluation criteria, on which the auction will be conducted;</td>
        <td markdown=1>

1. Set `tender/techniques/hasElectronicAuction` to `true`
1. Enter *the rules, including identification of the elements of the tender related to the evaluation criteria, on which the auction will be conducted* in `tender/techniques/electronicAuction/description`

This requires the [Techniques](https://github.com/open-contracting-extensions/ocds_techniques_extension) extension.

</td>
      </tr>
      <tr id="X:7(f)">
        <td>X:7(f)</td>
        <td>where there will be a public opening of tenders, the date, time and place for the opening and, where appropriate, the persons authorized to be present;</td>
        <td markdown=1>

1. Enter the *date* and the *time* in `tender/bidOpening/date`
1. Enter the *place* in `tender/bidOpening/address`, `tender/bidOpening/location` or `tender/bidOpening/gazetteer`
1. Enter *the persons authorized to be present* in `tender/bidOpening/description`

This requires the [Bid Opening](https://github.com/open-contracting-extensions/ocds_bidOpening_extension) extension.

</td>
      </tr>
      <tr id="X:7(g)">
        <td>X:7(g)</td>
        <td>any other terms or conditions, including terms of payment and any limitation on the means by which tenders may be submitted, such as whether on paper or by electronic means; and</td>
        <td markdown=1>

1. Enter the *terms of payment* in `tender/participationFees`
1. Enter *the means by which tenders may be submitted* in `tender/submissionMethod`:
    1. If it's *on paper*, enter 'written'
    1. If it's *by electronic means*, enter 'electronicSubmission'

This requires the [Participation Fees](https://github.com/open-contracting-extensions/ocds_participationFees_extension) extension.

</td>
      </tr>
      <tr id="X:7(h)">
        <td>X:7(h)</td>
        <td>any dates for the delivery of goods or the supply of services</td>
        <td markdown=1>

1. Follow the guidance for [VII:2(e)](#VII:2(e))

</td>
      </tr>
      <tr id="X:9">
        <td>X:9</td>
        <td>The evaluation criteria set out in the notice of intended procurement or tender documentation may include, among others, price and other cost factors, quality, technical merit, environmental characteristics and terms of delivery</td>
        <td markdown=1>

1. Enter the *evaluation criteria set out in the notice of intended procurement or tender documentation* in `tender/awardCriteriaDetails`
1. If the *evaluation criteria* are published as a document:
    1. Add a `Document` object to the `tender/documents` array
    1. Set its `documentType` to 'evaluationCriteria'
    1. Fill any other known information for the document ([`Document` object schema](https://standard.open-contracting.org/1.1/en/schema/reference/#document))

</td>
      </tr>
    </tbody>
  </table>
</div>

### Modifications

<div class="wy-table-responsive">
  <table class="docutils">
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
      <tr id="X:11">
        <td>X:11</td>
        <td>Where, prior to the award of a contract, a procuring entity modifies the criteria or requirements set out in the notice of intended procurement or tender documentation provided to participating suppliers, or amends or reissues a notice or tender documentation, it shall transmit in writing all such modifications or amended or re-issued notice or tender documentation: (a) to all suppliers that are participating at the time of the modification, amendment or re-issuance, where such suppliers are known to the entity, and in all other cases, in the same manner as the original information was made available; and (b) in adequate time to allow such suppliers to modify and re-submit amended tenders, as appropriate.</td>
        <td markdown=1>

1. [Create a new OCDS release](../operations/#create-a-release) and follow the corresponding guidance, depending on the information that has been modified:
    1. If the *the criteria or requirements* are modified, follow the guidance for [X:9](#X:9), and add 'tenderAmendment' to the `tag` array
    1. If *a notice* (of intended procurement) is amended or reissued, follow the guidance for [VII:2](#VII:2), but instead add 'tenderAmendment' to the `tag` array
    1. If the *tender documentation* is amended or reissued, follow the guidance for [X:7](#X:7), but instead add 'tenderAmendment' to the `tag` array

</td>
      </tr>
    </tbody>
  </table>
</div>

## [Article XIII](https://www.wto.org/english/docs_e/legal_e/rev-gpr-94_01_e.htm#articleXIII) Limited Tendering

<div class="wy-table-responsive">
  <table class="docutils">
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
      <tr id="XIII:2">
        <td>XIII:2</td>
        <td>A procuring entity shall prepare a report in writing on each contract awarded under paragraph 1. The report shall include the name of the procuring entity, the value and kind of goods or services procured and a statement indicating the circumstances and conditions described in paragraph 1 that justified the use of limited tendering.</td>
        <td markdown=1>

1. [Create an OCDS release](../operations/#create-a-release)
1. Add 'award' to the `tag` array
1. Set `tender/status` to 'complete'
1. If the following data has not been published following the guidance for VII:2
    1. For *the name of the procuring entity*, follow the guidance for [VII:2(a)](#VII:2(a))
    1. For the *kind of goods or services procured*, follow the guidance for [VII:2(b)](#VII:2(b))
1. Add an `Award` object to the `awards` array
    1. Enter an identifier in its `id`, which can be arbitrary as it is primarily to allow referencing from other parts of the file
    1. Enter the *kind of goods or services procured* in its `description` or, if possible, split it into `Item` objects in its `items` array.
    1. Enter *the value [of the goods or services]* in its `value/amount`
    1. Enter the currency in `value/currency` (see the [currency](https://standard.open-contracting.org/latest/en/schema/codelists/#currency) codelist)
    1. If the *report in writing* is also published as a document
        1. Add a `Document` object to its `documents` array
        1. Set its `documentType` to 'awardNotice'
        1. Fill any other known information for the document ([`Document` object schema](https://standard.open-contracting.org/1.1/en/schema/reference/#document))
1. Enter *the circumstances and conditions described in paragraph 1 that justified the use of limited tendering* in `tender/procurementMethodRationale`

</td>
      </tr>
    </tbody>
  </table>
</div>

## [Article XIV](https://www.wto.org/english/docs_e/legal_e/rev-gpr-94_01_e.htm#articleXIV) Electronic Auctions

<div class="wy-table-responsive">
  <table class="docutils">
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
      <tr id="XIV:1">
        <td>XIV:1</td>
        <td colspan="2">Where a procuring entity intends to conduct a covered procurement using an electronic auction, the entity shall provide each participant, before commencing the electronic auction, with:</td>
      </tr>
      <tr id="XIV:1(a)">
        <td>XIV:1(a)</td>
        <td>the automatic evaluation method, including the mathematical formula, that is based on the evaluation criteria set out in the tender documentation and that will be used in the automatic ranking or re-ranking during the auction;</td>
        <td markdown=1>

1. [Create an OCDS release](../operations/#create-a-release)
1. Enter or append *the automatic evaluation method, including the mathematical formula* in `tender/techniques/electronicAuction/description`

</td>
      </tr>
      <tr id="XIV:1(b)">
        <td>XIV:1(b)</td>
        <td>the results of any initial evaluation of the elements of its tender where the contract is to be awarded on the basis of the most advantageous tender;  and</td>
        <td markdown=1>

1. If *the results of any initial evaluation of the elements of [each participant's] tender* are published as a document:
    1. Add a `Document` object to the award's `documents` array
    1. Set its `documentType` to 'evaluationReports'
    1. Fill any other known information for the document ([`Document` object schema](https://standard.open-contracting.org/1.1/en/schema/reference/#document))

</td>
      </tr>
      <tr id="XIV:1(c)">
        <td>XIV:1(c)</td>
        <td>any other relevant information relating to the conduct of the auction.</td>
        <td markdown=1>

1. Enter or append *any other relevant information relating to the conduct of the auction* in `tender/techniques/electronicAuction/description`

</td>
      </tr>
    </tbody>
  </table>
</div>

## [Article XVI](https://www.wto.org/english/docs_e/legal_e/rev-gpr-94_01_e.htm#articleXVI) Transparency of Procurement Information

### Publication of Award Information

<div class="wy-table-responsive">
  <table class="docutils">
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
      <tr id="XVI:2">
        <td>XVI:2</td>
        <td colspan="2">Not later than 72 days after the award of each contract covered by this Agreement, a procuring entity shall publish a notice in the appropriate paper or electronic medium listed in Appendix III. Where the entity publishes the notice only in an electronic medium, the information shall remain readily accessible for a reasonable period of time. The notice shall include at least the following information:</td>
      </tr>
      <tr id="XVI:2(a)">
        <td>XVI:2(a)</td>
        <td>a description of the goods or services procured;</td>
        <td markdown=1>

1. [Create an OCDS release](../operations/#create-a-release)
1. Add 'award' to the `tag` array
1. Set `tender/status` to 'complete'
1. Add an `Award` object to the `awards` array
    1. Enter an identifier in its `id`, which can be arbitrary as it is primarily to allow referencing from other parts of the file
    1. Enter the *description of the goods or services procured* in its `description` or, if possible, split it into `Item` objects in its `items` array.

</td>
      </tr>
      <tr id="XVI:2(b)">
        <td>XVI:2(b)</td>
        <td>the name and address of the procuring entity;</td>
        <td markdown=1>

1. Follow the guidance for [VII:2(a)](#VII:2(a))

</td>
      </tr>
      <tr id="XVI:2(c)">
        <td>XVI:2(c)</td>
        <td>the name and address of the successful supplier;</td>
        <td markdown=1>

1. Add an `Organization` object to the `parties` array:
    1. Add 'supplier' to its `roles`
    1. Enter an identifier in its `id`, which can be arbitrary as it is primarily to allow referencing from other parts of the file
    1. Enter the *name* in its `name`
    1. Enter the *address* in its `address`
1. Add an `OrganizationReference` object to the award's `suppliers` array:
    1. Enter the organization `id` of the supplier in its `id`
    1. Enter the *name* of the supplier in its `name`

</td>
      </tr>
      <tr id="XVI:2(d)">
        <td>XVI:2(d)</td>
        <td>the value of the successful tender or the highest and lowest offers taken into account in the award of the contract;</td>
        <td markdown=1>

1. Enter *the value of the successful tender* in the award's `value/amount`
1. Enter the currency in the award's `value/currency` (see the [currency](https://standard.open-contracting.org/latest/en/schema/codelists/#currency) codelist
1. For *the highest offer taken into account in the award of the contract*, add a `BidsStatistic` object to the `bids/statistics` array:
    1. Enter an identifier in its `id`, which can be arbitrary as it is primarily to allow referencing from other parts of the file
    1. Enter the value of the offer in its `value`
    1. Enter the currency of the offer in its `currency`
    1. Set its `measure` to `highestValidBidValue`
1. For *the lowest offer taken into account in the award of the contract*, repeat the above guidance and set `measure` to `lowestValidBidValue`

</td>
      </tr>
      <tr id="XVI:2(e)">
        <td>XVI:2(e)</td>
        <td>the date of award; and</td>
        <td markdown=1>

1. Enter *the date of the award* in the award's `date`

</td>
      </tr>
      <tr id="XVI:2(f)">
        <td>XVI:2(f)</td>
        <td>the type of procurement method used, and in cases where limited tendering was used in accordance with Article XIII, a description of the circumstances justifying the use of limited tendering.</td>
        <td markdown=1>

1. For *the type of procurement method used*, follow the guidance for [VII:2(f)](#VII:2(f))
1. For *description of the circumstances justifying the use of limited tendering*, follow the guidance for [XIII:2](#XIII:2)

</td>
      </tr>
    </tbody>
  </table>
</div>

### Collection and Reporting of Statistics

<div class="wy-table-responsive">
  <table class="docutils">
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
        <td>XVI:4</td>
        <td>Each Party shall collect and report to the Committee statistics on its contracts covered by this Agreement. Each report shall cover one year and be submitted within two years of the end of the reporting period, and shall contain:</td>
        <td rowspan="7" markdown=1>

If you are interested in calculating statistics using OCDS data, please contact <data@open-contracting.org> or comment on this [GitHub issue](https://github.com/open-contracting-extensions/government-procurement-agreement/issues/45).

In the meantime, you might be interested in this [Python notebook](http://bit.ly/OCPaustraliaexample), which demonstrates how to calculate statistics using Australia's data.

</td>
      </tr>
      <tr id="XVI:4(a)">
        <td>XVI:4(a)</td>
        <td>for Annex 1 procuring entities:</td>
      </tr>
      <tr id="XVI:4(a)">
        <td>XVI:4(a)(i)</td>
        <td>the number and total value, for all such entities, of all contracts covered by this Agreement;</td>
      </tr>
      <tr id="XVI:4(a)">
        <td>XVI:4(a)(ii)</td>
        <td>the number and total value of all contracts covered by this Agreement awarded by each such entity, broken down by categories of goods and services according to an internationally recognized uniform classification system;  and</td>
      </tr>
      <tr id="XVI:4(a)">
        <td>XVI:4(a)(iii)</td>
        <td>the number and total value of all contracts covered by this Agreement awarded by each such entity under limited tendering;</td>
      </tr>
      <tr id="XVI:4(b)">
        <td>XVI:4(b)</td>
        <td>for Annex 2 and 3 procuring entities, the number and total value of contracts covered by this Agreement awarded by all such entities, broken down by Annex;  and</td>
      </tr>
      <tr id="XVI:4(c)">
        <td>XVI:4(c)</td>
        <td>estimates for the data required under subparagraphs (a) and (b), with an explanation of the methodology used to develop the estimates, where it is not feasible to provide the data.</td>
      </tr>
    </tbody>
  </table>
</div>
