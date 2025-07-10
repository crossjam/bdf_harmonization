# Overview of the data in our system you are harmonizing against

Our system is designed to harmonized a users data against a common data element (CDE). A CDE is an entity that comes in two flavours - those with a controlled vocabulary (commonly called permissible values) and those without. Below is an example of both:

CDE with permissible values:
```jsonc
{
    "embedding_medium": {
        "description": "A material that infiltrates and supports a specimen and preserves its shape and structure for sectioning and microscopy.",
        "permissible_values": [
            "Paraffin wax",
            "Carbowax",
            "Methacrylate",
            "Epoxy Resin (Araldite)",
            "Agar embedding",
            "Celloidin media",
            "Gelatin",
            "Other",
            "None",
            "Unknown"
        ]
    }
}
```

CDE without permissible values:
```jsonc
{
    "participant_id": {
        "description": "A number or a string that may contain metadata information, for a participant who has taken part in the investigation or study.",
        "permissible_values": []
    }
}
```

An easy way to visualize these is to think of the CDE, such as `embedding_medium` as a column header in a spreadsheet. While the permissible values, such as `Carbowax` and `Agar embedding` as values in the rows below that header. In the case of the `participant_id` header the values in its column will simply be whatever the data creator entered.


The **/harmonize** endpoint is designed to standardize a free-text string, typically a value from a spreadsheet, to one of the permissible values for a selected CDE.
- For more details on the harmonize endpoint please see the documentation here: <...>
- For code examples of various use cases involving this endpoint please see the documentation here: <...>


These CDEs are typically grouped into schemas, examples of such groupings can be seen in the NCI's General Commons (GC) data model (https://github.com/CBIIT/cds-model/blob/main/model-desc/cds-model-props.yml), which consists of approximately 250 CDEs. While smaller sub schemas can be created from a larger data model - in the case of the Neurofibramatosis data model (https://github.com/nf-osi/nf-metadata-dictionary), curated by Sage Bionetworks, where they have created smaller schemas for specific purposes. Such as their RNA Seq schema (https://github.com/nf-osi/nf-metadata-dictionary/blob/batch-convert/registered-json-schemas/RNASeqTemplate-deref.json) comprising of 69 CDEs or their Imaging Assay schema (https://github.com/nf-osi/nf-metadata-dictionary/blob/batch-convert/registered-json-schemas/ImagingAssayTemplate-deref.json) consisting of 40 CDEs.

Currently our system has the following schemas loaded:
- NCI's General Commons (version 6.0.4)
- NCI's Cancer Data Services (Version 5.0.2)
- 4 sub-schemas of the Larger Neurofibramatosis data model
    - RNA Seq
    - Imaging Assay
    - Clinical Assay
    - ChIP Seq


Figuring out what schema and/or CDE to harmonize some data against can be done with the **/cde-recommendation** endpoint.
- For mored details on the cde-recommendation endpoint please see the documenation here: <...>
- For code examples of various use cases involving this endpoint please see the documentation here: <...>

Our system is designed to be flexible and scalable in order to accomodate almost any schema and CDEs. If you are interested in having your own data loaded into our system please reach out to use via the following steps: <Requesting Adding Data to the API>