def ingest_documents():

    try:

        count = collection.count()

        logger.info(f"Current document count: {count}")

        if count > 0:
            logger.info("Skipping ingestion.")
            return

        docs_folder = Path("docs")

        if not docs_folder.exists():
            logger.error("docs folder not found")
            return

        docs = []
        ids = []
        metadatas = []

        for file in docs_folder.glob("*.txt"):

            logger.info(f"Reading {file.name}")

            content = file.read_text(
                encoding="utf-8"
            )

            docs.append(content)
            ids.append(file.stem)
            metadatas.append({
                "source": file.name
            })

        if docs:

            collection.add(
                ids=ids,
                documents=docs,
                metadatas=metadatas
            )

        logger.info(
            f"Ingested {len(docs)} documents"
        )

    except Exception as e:
        logger.exception(
            f"Ingestion failed: {e}"
        )
