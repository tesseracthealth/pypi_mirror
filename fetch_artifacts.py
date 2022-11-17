import wget

_artifacts = [
    "https://github.com/open-telemetry/opentelemetry-collector-releases/releases/download/v0.63.1/otelcol_0.63.1_linux_arm64.deb",    
    "https://files.pythonhosted.org/packages/e2/8d/e4ec67448273652daaac38f0b77c4778178ad16c01294e13f4065c1487e1/opentelemetry_api-1.13.0-py3-none-any.whl",    
    "https://files.pythonhosted.org/packages/fb/6a/98c8c21ddfa96a27fefe641d344309d91ebf7c0588731399e3211e1055dd/opentelemetry_instrumentation-0.35b0-py3-none-any.whl",
    "https://files.pythonhosted.org/packages/ab/4c/38bfbde3d6be17026f96a7e90528a188b6461d7143dead046feab116701b/opentelemetry_instrumentation_grpc-0.35b0-py3-none-any.whl",    
    "https://files.pythonhosted.org/packages/df/73/b6e24bd22e6720ca8ee9a85a0c4a2971af8497d8f3193fa05390cbd46e09/backoff-2.2.1-py3-none-any.whl",
    "https://files.pythonhosted.org/packages/e2/fd/d9efa2085bd762fba3a637eb3e36d76d72eb6e083d170aeaca65a75f1f9c/googleapis_common_protos-1.56.4-py2.py3-none-any.whl", 
    "https://files.pythonhosted.org/packages/f3/5c/13a5c750d0d54983f7e5e37f895d0e516106aed5fcda6c5129bd8ee8848f/opentelemetry_exporter_otlp-1.13.0-py3-none-any.whl",
    "https://files.pythonhosted.org/packages/6d/63/aa77a9fdd1b6273a0dcf2346cb8b599a79d1b2fec606815e252014e83e27/opentelemetry_exporter_otlp_proto_grpc-1.13.0-py3-none-any.whl",
    "https://files.pythonhosted.org/packages/00/69/513b301f9d404d749ac9f593afd50e84fefc0d1d0af543fb342e55d1effe/opentelemetry_proto-1.13.0-py3-none-any.whl",
    "https://files.pythonhosted.org/packages/73/8a/b4a61c354ac5c008c68c9095945a6bebb008f65ad1f4ca95161cf3d9d290/opentelemetry_sdk-1.13.0-py3-none-any.whl",
    "https://files.pythonhosted.org/packages/8f/33/53ee2bf33797acd075f29abec884c9022eb944d8b3f21a61958199744b9d/opentelemetry_semantic_conventions-0.35b0-py3-none-any.whl",        
    "https://files.pythonhosted.org/packages/03/97/f58c723ff036a8d8b4d3115377c0a37ed05c1f68dd9a0d66dab5e82c5c1c/build-0.9.0-py3-none-any.whl",
    "https://files.pythonhosted.org/packages/1d/e3/fa60c47d7c344533142eb3af0b73234ef8ea3fb2da742ab976b947e717df/bump2version-1.0.1-py2.py3-none-any.whl",    
    "https://files.pythonhosted.org/packages/ee/2f/ef63e64e9429111e73d3d6cbee80591672d16f2725e648ebc52096f3d323/pep517-0.13.0-py3-none-any.whl",    
]




def mainline():
    for each in _artifacts:
        print(f"Fetching {each}")
        filename = wget.download(each)        
        print(f"Downloaded {filename}")


if __name__ == "__main__":
    mainline()