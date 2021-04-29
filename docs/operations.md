# Common operations

To avoid repetition in the guidance, we refer and link to the following common operations.

## Create a release

1. Set `id` to the [release ID](https://standard.open-contracting.org/latest/en/schema/identifiers/#release-id).
1. Set `initiationType` to 'tender'.
1. Set [`ocid`](https://standard.open-contracting.org/latest/en/schema/identifiers/#contracting-process-identifier-ocid) as described below.

The notice's `ocid` will either be a new `ocid`, or the same `ocid` as the previous publication concerning this procedure. The notice's `ocid` will be a new `ocid` if one of the following is true:

* The notice is the first publication concerning the procedure.
* The notice is a contract award notice for an award within a framework agreement or dynamic purchasing system.

If none is true, then set the notice's `ocid` to be the same as the previous publication's `ocid`. Otherwise, set the notice's [`ocid`](https://standard.open-contracting.org/latest/en/schema/identifiers/#contracting-process-identifier-ocid) by prepending your [OCID prefix](https://standard.open-contracting.org/latest/en/guidance/build/#register-an-ocid-prefix) to a unique identifier of your choice (e.g. a [version 4 UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier) or a suitable system-internal identifier).

If the notice is a contract award notice for an award within a framework agreement or dynamic purchasing system, you must also add a `RelatedProcess` object to the `relatedProcesses` array, set its `.id` to '1', add 'framework' to its `.relationship` array, set its `.scheme` to 'ocid', and set its `.identifier` to the `ocid` of the procedure that set up the framework agreement or dynamic purchasing system.
