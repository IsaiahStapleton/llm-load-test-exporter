# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: generation.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x10generation.proto\x12\x05\x66maas"\xa1\x01\n\x18\x42\x61tchedGenerationRequest\x12\x10\n\x08model_id\x18\x01 \x01(\t\x12\x16\n\tprefix_id\x18\x02 \x01(\tH\x00\x88\x01\x01\x12*\n\x08requests\x18\x03 \x03(\x0b\x32\x18.fmaas.GenerationRequest\x12!\n\x06params\x18\n \x01(\x0b\x32\x11.fmaas.ParametersB\x0c\n\n_prefix_id"\x9f\x01\n\x17SingleGenerationRequest\x12\x10\n\x08model_id\x18\x01 \x01(\t\x12\x16\n\tprefix_id\x18\x02 \x01(\tH\x00\x88\x01\x01\x12)\n\x07request\x18\x03 \x01(\x0b\x32\x18.fmaas.GenerationRequest\x12!\n\x06params\x18\n \x01(\x0b\x32\x11.fmaas.ParametersB\x0c\n\n_prefix_id"I\n\x19\x42\x61tchedGenerationResponse\x12,\n\tresponses\x18\x01 \x03(\x0b\x32\x19.fmaas.GenerationResponse"!\n\x11GenerationRequest\x12\x0c\n\x04text\x18\x02 \x01(\t"\xf3\x01\n\x12GenerationResponse\x12\x19\n\x11input_token_count\x18\x06 \x01(\r\x12\x1d\n\x15generated_token_count\x18\x02 \x01(\r\x12\x0c\n\x04text\x18\x04 \x01(\t\x12&\n\x0bstop_reason\x18\x07 \x01(\x0e\x32\x11.fmaas.StopReason\x12\x15\n\rstop_sequence\x18\x0b \x01(\t\x12\x0c\n\x04seed\x18\n \x01(\x04\x12 \n\x06tokens\x18\x08 \x03(\x0b\x32\x10.fmaas.TokenInfo\x12&\n\x0cinput_tokens\x18\t \x03(\x0b\x32\x10.fmaas.TokenInfo"\x81\x02\n\nParameters\x12%\n\x06method\x18\x01 \x01(\x0e\x32\x15.fmaas.DecodingMethod\x12+\n\x08sampling\x18\x02 \x01(\x0b\x32\x19.fmaas.SamplingParameters\x12)\n\x08stopping\x18\x03 \x01(\x0b\x32\x17.fmaas.StoppingCriteria\x12(\n\x08response\x18\x04 \x01(\x0b\x32\x16.fmaas.ResponseOptions\x12+\n\x08\x64\x65\x63oding\x18\x05 \x01(\x0b\x32\x19.fmaas.DecodingParameters\x12\x1d\n\x15truncate_input_tokens\x18\x06 \x01(\r"\xc5\x01\n\x12\x44\x65\x63odingParameters\x12\x1a\n\x12repetition_penalty\x18\x01 \x01(\x02\x12\x44\n\x0elength_penalty\x18\x02 \x01(\x0b\x32\'.fmaas.DecodingParameters.LengthPenaltyH\x00\x88\x01\x01\x1a:\n\rLengthPenalty\x12\x13\n\x0bstart_index\x18\x01 \x01(\r\x12\x14\n\x0c\x64\x65\x63\x61y_factor\x18\x02 \x01(\x02\x42\x11\n\x0f_length_penalty"v\n\x12SamplingParameters\x12\x13\n\x0btemperature\x18\x01 \x01(\x02\x12\r\n\x05top_k\x18\x02 \x01(\r\x12\r\n\x05top_p\x18\x03 \x01(\x02\x12\x11\n\ttypical_p\x18\x04 \x01(\x02\x12\x11\n\x04seed\x18\x05 \x01(\x04H\x00\x88\x01\x01\x42\x07\n\x05_seed"\xb3\x01\n\x10StoppingCriteria\x12\x16\n\x0emax_new_tokens\x18\x01 \x01(\r\x12\x16\n\x0emin_new_tokens\x18\x02 \x01(\r\x12\x19\n\x11time_limit_millis\x18\x03 \x01(\r\x12\x16\n\x0estop_sequences\x18\x04 \x03(\t\x12"\n\x15include_stop_sequence\x18\x05 \x01(\x08H\x00\x88\x01\x01\x42\x18\n\x16_include_stop_sequence"\x98\x01\n\x0fResponseOptions\x12\x12\n\ninput_text\x18\x01 \x01(\x08\x12\x18\n\x10generated_tokens\x18\x02 \x01(\x08\x12\x14\n\x0cinput_tokens\x18\x03 \x01(\x08\x12\x16\n\x0etoken_logprobs\x18\x04 \x01(\x08\x12\x13\n\x0btoken_ranks\x18\x05 \x01(\x08\x12\x14\n\x0ctop_n_tokens\x18\x06 \x01(\r"\x92\x01\n\tTokenInfo\x12\x0c\n\x04text\x18\x02 \x01(\t\x12\x0f\n\x07logprob\x18\x03 \x01(\x02\x12\x0c\n\x04rank\x18\x04 \x01(\r\x12-\n\ntop_tokens\x18\x05 \x03(\x0b\x32\x19.fmaas.TokenInfo.TopToken\x1a)\n\x08TopToken\x12\x0c\n\x04text\x18\x02 \x01(\t\x12\x0f\n\x07logprob\x18\x03 \x01(\x02"k\n\x16\x42\x61tchedTokenizeRequest\x12\x10\n\x08model_id\x18\x01 \x01(\t\x12(\n\x08requests\x18\x02 \x03(\x0b\x32\x16.fmaas.TokenizeRequest\x12\x15\n\rreturn_tokens\x18\x03 \x01(\x08"E\n\x17\x42\x61tchedTokenizeResponse\x12*\n\tresponses\x18\x01 \x03(\x0b\x32\x17.fmaas.TokenizeResponse"\x1f\n\x0fTokenizeRequest\x12\x0c\n\x04text\x18\x01 \x01(\t"7\n\x10TokenizeResponse\x12\x13\n\x0btoken_count\x18\x01 \x01(\r\x12\x0e\n\x06tokens\x18\x02 \x03(\t"$\n\x10ModelInfoRequest\x12\x10\n\x08model_id\x18\x01 \x01(\t"\xb4\x01\n\x11ModelInfoResponse\x12\x36\n\nmodel_kind\x18\x01 \x01(\x0e\x32".fmaas.ModelInfoResponse.ModelKind\x12\x1b\n\x13max_sequence_length\x18\x02 \x01(\r\x12\x16\n\x0emax_new_tokens\x18\x03 \x01(\r"2\n\tModelKind\x12\x10\n\x0c\x44\x45\x43ODER_ONLY\x10\x00\x12\x13\n\x0f\x45NCODER_DECODER\x10\x01*(\n\x0e\x44\x65\x63odingMethod\x12\n\n\x06GREEDY\x10\x00\x12\n\n\x06SAMPLE\x10\x01*\x8b\x01\n\nStopReason\x12\x10\n\x0cNOT_FINISHED\x10\x00\x12\x0e\n\nMAX_TOKENS\x10\x01\x12\r\n\tEOS_TOKEN\x10\x02\x12\r\n\tCANCELLED\x10\x03\x12\x0e\n\nTIME_LIMIT\x10\x04\x12\x11\n\rSTOP_SEQUENCE\x10\x05\x12\x0f\n\x0bTOKEN_LIMIT\x10\x06\x12\t\n\x05\x45RROR\x10\x07\x32\xc4\x02\n\x11GenerationService\x12O\n\x08Generate\x12\x1f.fmaas.BatchedGenerationRequest\x1a .fmaas.BatchedGenerationResponse"\x00\x12O\n\x0eGenerateStream\x12\x1e.fmaas.SingleGenerationRequest\x1a\x19.fmaas.GenerationResponse"\x00\x30\x01\x12K\n\x08Tokenize\x12\x1d.fmaas.BatchedTokenizeRequest\x1a\x1e.fmaas.BatchedTokenizeResponse"\x00\x12@\n\tModelInfo\x12\x17.fmaas.ModelInfoRequest\x1a\x18.fmaas.ModelInfoResponse"\x00\x62\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "generation_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _globals["_DECODINGMETHOD"]._serialized_start = 2266
    _globals["_DECODINGMETHOD"]._serialized_end = 2306
    _globals["_STOPREASON"]._serialized_start = 2309
    _globals["_STOPREASON"]._serialized_end = 2448
    _globals["_BATCHEDGENERATIONREQUEST"]._serialized_start = 28
    _globals["_BATCHEDGENERATIONREQUEST"]._serialized_end = 189
    _globals["_SINGLEGENERATIONREQUEST"]._serialized_start = 192
    _globals["_SINGLEGENERATIONREQUEST"]._serialized_end = 351
    _globals["_BATCHEDGENERATIONRESPONSE"]._serialized_start = 353
    _globals["_BATCHEDGENERATIONRESPONSE"]._serialized_end = 426
    _globals["_GENERATIONREQUEST"]._serialized_start = 428
    _globals["_GENERATIONREQUEST"]._serialized_end = 461
    _globals["_GENERATIONRESPONSE"]._serialized_start = 464
    _globals["_GENERATIONRESPONSE"]._serialized_end = 707
    _globals["_PARAMETERS"]._serialized_start = 710
    _globals["_PARAMETERS"]._serialized_end = 967
    _globals["_DECODINGPARAMETERS"]._serialized_start = 970
    _globals["_DECODINGPARAMETERS"]._serialized_end = 1167
    _globals["_DECODINGPARAMETERS_LENGTHPENALTY"]._serialized_start = 1090
    _globals["_DECODINGPARAMETERS_LENGTHPENALTY"]._serialized_end = 1148
    _globals["_SAMPLINGPARAMETERS"]._serialized_start = 1169
    _globals["_SAMPLINGPARAMETERS"]._serialized_end = 1287
    _globals["_STOPPINGCRITERIA"]._serialized_start = 1290
    _globals["_STOPPINGCRITERIA"]._serialized_end = 1469
    _globals["_RESPONSEOPTIONS"]._serialized_start = 1472
    _globals["_RESPONSEOPTIONS"]._serialized_end = 1624
    _globals["_TOKENINFO"]._serialized_start = 1627
    _globals["_TOKENINFO"]._serialized_end = 1773
    _globals["_TOKENINFO_TOPTOKEN"]._serialized_start = 1732
    _globals["_TOKENINFO_TOPTOKEN"]._serialized_end = 1773
    _globals["_BATCHEDTOKENIZEREQUEST"]._serialized_start = 1775
    _globals["_BATCHEDTOKENIZEREQUEST"]._serialized_end = 1882
    _globals["_BATCHEDTOKENIZERESPONSE"]._serialized_start = 1884
    _globals["_BATCHEDTOKENIZERESPONSE"]._serialized_end = 1953
    _globals["_TOKENIZEREQUEST"]._serialized_start = 1955
    _globals["_TOKENIZEREQUEST"]._serialized_end = 1986
    _globals["_TOKENIZERESPONSE"]._serialized_start = 1988
    _globals["_TOKENIZERESPONSE"]._serialized_end = 2043
    _globals["_MODELINFOREQUEST"]._serialized_start = 2045
    _globals["_MODELINFOREQUEST"]._serialized_end = 2081
    _globals["_MODELINFORESPONSE"]._serialized_start = 2084
    _globals["_MODELINFORESPONSE"]._serialized_end = 2264
    _globals["_MODELINFORESPONSE_MODELKIND"]._serialized_start = 2214
    _globals["_MODELINFORESPONSE_MODELKIND"]._serialized_end = 2264
    _globals["_GENERATIONSERVICE"]._serialized_start = 2451
    _globals["_GENERATIONSERVICE"]._serialized_end = 2775
# @@protoc_insertion_point(module_scope)