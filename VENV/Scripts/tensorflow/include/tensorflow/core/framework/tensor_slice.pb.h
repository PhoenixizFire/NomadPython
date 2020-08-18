// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: tensorflow/core/framework/tensor_slice.proto

#ifndef GOOGLE_PROTOBUF_INCLUDED_tensorflow_2fcore_2fframework_2ftensor_5fslice_2eproto
#define GOOGLE_PROTOBUF_INCLUDED_tensorflow_2fcore_2fframework_2ftensor_5fslice_2eproto

#include <limits>
#include <string>

#include <google/protobuf/port_def.inc>
#if PROTOBUF_VERSION < 3009000
#error This file was generated by a newer version of protoc which is
#error incompatible with your Protocol Buffer headers. Please update
#error your headers.
#endif
#if 3009002 < PROTOBUF_MIN_PROTOC_VERSION
#error This file was generated by an older version of protoc which is
#error incompatible with your Protocol Buffer headers. Please
#error regenerate this file with a newer version of protoc.
#endif

#include <google/protobuf/port_undef.inc>
#include <google/protobuf/io/coded_stream.h>
#include <google/protobuf/arena.h>
#include <google/protobuf/arenastring.h>
#include <google/protobuf/generated_message_table_driven.h>
#include <google/protobuf/generated_message_util.h>
#include <google/protobuf/inlined_string_field.h>
#include <google/protobuf/metadata.h>
#include <google/protobuf/generated_message_reflection.h>
#include <google/protobuf/message.h>
#include <google/protobuf/repeated_field.h>  // IWYU pragma: export
#include <google/protobuf/extension_set.h>  // IWYU pragma: export
#include <google/protobuf/unknown_field_set.h>
// @@protoc_insertion_point(includes)
#include <google/protobuf/port_def.inc>
#define PROTOBUF_INTERNAL_EXPORT_tensorflow_2fcore_2fframework_2ftensor_5fslice_2eproto
PROTOBUF_NAMESPACE_OPEN
namespace internal {
class AnyMetadata;
}  // namespace internal
PROTOBUF_NAMESPACE_CLOSE

// Internal implementation detail -- do not use these members.
struct TableStruct_tensorflow_2fcore_2fframework_2ftensor_5fslice_2eproto {
  static const ::PROTOBUF_NAMESPACE_ID::internal::ParseTableField entries[]
    PROTOBUF_SECTION_VARIABLE(protodesc_cold);
  static const ::PROTOBUF_NAMESPACE_ID::internal::AuxillaryParseTableField aux[]
    PROTOBUF_SECTION_VARIABLE(protodesc_cold);
  static const ::PROTOBUF_NAMESPACE_ID::internal::ParseTable schema[2]
    PROTOBUF_SECTION_VARIABLE(protodesc_cold);
  static const ::PROTOBUF_NAMESPACE_ID::internal::FieldMetadata field_metadata[];
  static const ::PROTOBUF_NAMESPACE_ID::internal::SerializationTable serialization_table[];
  static const ::PROTOBUF_NAMESPACE_ID::uint32 offsets[];
};
extern const ::PROTOBUF_NAMESPACE_ID::internal::DescriptorTable descriptor_table_tensorflow_2fcore_2fframework_2ftensor_5fslice_2eproto;
namespace tensorflow {
class TensorSliceProto;
class TensorSliceProtoDefaultTypeInternal;
extern TensorSliceProtoDefaultTypeInternal _TensorSliceProto_default_instance_;
class TensorSliceProto_Extent;
class TensorSliceProto_ExtentDefaultTypeInternal;
extern TensorSliceProto_ExtentDefaultTypeInternal _TensorSliceProto_Extent_default_instance_;
}  // namespace tensorflow
PROTOBUF_NAMESPACE_OPEN
template<> ::tensorflow::TensorSliceProto* Arena::CreateMaybeMessage<::tensorflow::TensorSliceProto>(Arena*);
template<> ::tensorflow::TensorSliceProto_Extent* Arena::CreateMaybeMessage<::tensorflow::TensorSliceProto_Extent>(Arena*);
PROTOBUF_NAMESPACE_CLOSE
namespace tensorflow {

// ===================================================================

class TensorSliceProto_Extent :
    public ::PROTOBUF_NAMESPACE_ID::Message /* @@protoc_insertion_point(class_definition:tensorflow.TensorSliceProto.Extent) */ {
 public:
  TensorSliceProto_Extent();
  virtual ~TensorSliceProto_Extent();

  TensorSliceProto_Extent(const TensorSliceProto_Extent& from);
  TensorSliceProto_Extent(TensorSliceProto_Extent&& from) noexcept
    : TensorSliceProto_Extent() {
    *this = ::std::move(from);
  }

  inline TensorSliceProto_Extent& operator=(const TensorSliceProto_Extent& from) {
    CopyFrom(from);
    return *this;
  }
  inline TensorSliceProto_Extent& operator=(TensorSliceProto_Extent&& from) noexcept {
    if (GetArenaNoVirtual() == from.GetArenaNoVirtual()) {
      if (this != &from) InternalSwap(&from);
    } else {
      CopyFrom(from);
    }
    return *this;
  }

  inline ::PROTOBUF_NAMESPACE_ID::Arena* GetArena() const final {
    return GetArenaNoVirtual();
  }
  inline void* GetMaybeArenaPointer() const final {
    return MaybeArenaPtr();
  }
  static const ::PROTOBUF_NAMESPACE_ID::Descriptor* descriptor() {
    return GetDescriptor();
  }
  static const ::PROTOBUF_NAMESPACE_ID::Descriptor* GetDescriptor() {
    return GetMetadataStatic().descriptor;
  }
  static const ::PROTOBUF_NAMESPACE_ID::Reflection* GetReflection() {
    return GetMetadataStatic().reflection;
  }
  static const TensorSliceProto_Extent& default_instance();

  enum HasLengthCase {
    kLength = 2,
    HAS_LENGTH_NOT_SET = 0,
  };

  static void InitAsDefaultInstance();  // FOR INTERNAL USE ONLY
  static inline const TensorSliceProto_Extent* internal_default_instance() {
    return reinterpret_cast<const TensorSliceProto_Extent*>(
               &_TensorSliceProto_Extent_default_instance_);
  }
  static constexpr int kIndexInFileMessages =
    0;

  friend void swap(TensorSliceProto_Extent& a, TensorSliceProto_Extent& b) {
    a.Swap(&b);
  }
  inline void Swap(TensorSliceProto_Extent* other) {
    if (other == this) return;
    if (GetArenaNoVirtual() == other->GetArenaNoVirtual()) {
      InternalSwap(other);
    } else {
      ::PROTOBUF_NAMESPACE_ID::internal::GenericSwap(this, other);
    }
  }
  void UnsafeArenaSwap(TensorSliceProto_Extent* other) {
    if (other == this) return;
    GOOGLE_DCHECK(GetArenaNoVirtual() == other->GetArenaNoVirtual());
    InternalSwap(other);
  }

  // implements Message ----------------------------------------------

  inline TensorSliceProto_Extent* New() const final {
    return CreateMaybeMessage<TensorSliceProto_Extent>(nullptr);
  }

  TensorSliceProto_Extent* New(::PROTOBUF_NAMESPACE_ID::Arena* arena) const final {
    return CreateMaybeMessage<TensorSliceProto_Extent>(arena);
  }
  void CopyFrom(const ::PROTOBUF_NAMESPACE_ID::Message& from) final;
  void MergeFrom(const ::PROTOBUF_NAMESPACE_ID::Message& from) final;
  void CopyFrom(const TensorSliceProto_Extent& from);
  void MergeFrom(const TensorSliceProto_Extent& from);
  PROTOBUF_ATTRIBUTE_REINITIALIZES void Clear() final;
  bool IsInitialized() const final;

  size_t ByteSizeLong() const final;
  #if GOOGLE_PROTOBUF_ENABLE_EXPERIMENTAL_PARSER
  const char* _InternalParse(const char* ptr, ::PROTOBUF_NAMESPACE_ID::internal::ParseContext* ctx) final;
  #else
  bool MergePartialFromCodedStream(
      ::PROTOBUF_NAMESPACE_ID::io::CodedInputStream* input) final;
  #endif  // GOOGLE_PROTOBUF_ENABLE_EXPERIMENTAL_PARSER
  void SerializeWithCachedSizes(
      ::PROTOBUF_NAMESPACE_ID::io::CodedOutputStream* output) const final;
  ::PROTOBUF_NAMESPACE_ID::uint8* InternalSerializeWithCachedSizesToArray(
      ::PROTOBUF_NAMESPACE_ID::uint8* target) const final;
  int GetCachedSize() const final { return _cached_size_.Get(); }

  private:
  inline void SharedCtor();
  inline void SharedDtor();
  void SetCachedSize(int size) const final;
  void InternalSwap(TensorSliceProto_Extent* other);
  friend class ::PROTOBUF_NAMESPACE_ID::internal::AnyMetadata;
  static ::PROTOBUF_NAMESPACE_ID::StringPiece FullMessageName() {
    return "tensorflow.TensorSliceProto.Extent";
  }
  protected:
  explicit TensorSliceProto_Extent(::PROTOBUF_NAMESPACE_ID::Arena* arena);
  private:
  static void ArenaDtor(void* object);
  inline void RegisterArenaDtor(::PROTOBUF_NAMESPACE_ID::Arena* arena);
  private:
  inline ::PROTOBUF_NAMESPACE_ID::Arena* GetArenaNoVirtual() const {
    return _internal_metadata_.arena();
  }
  inline void* MaybeArenaPtr() const {
    return _internal_metadata_.raw_arena_ptr();
  }
  public:

  ::PROTOBUF_NAMESPACE_ID::Metadata GetMetadata() const final;
  private:
  static ::PROTOBUF_NAMESPACE_ID::Metadata GetMetadataStatic() {
    ::PROTOBUF_NAMESPACE_ID::internal::AssignDescriptors(&::descriptor_table_tensorflow_2fcore_2fframework_2ftensor_5fslice_2eproto);
    return ::descriptor_table_tensorflow_2fcore_2fframework_2ftensor_5fslice_2eproto.file_level_metadata[kIndexInFileMessages];
  }

  public:

  // nested types ----------------------------------------------------

  // accessors -------------------------------------------------------

  enum : int {
    kStartFieldNumber = 1,
    kLengthFieldNumber = 2,
  };
  // int64 start = 1;
  void clear_start();
  ::PROTOBUF_NAMESPACE_ID::int64 start() const;
  void set_start(::PROTOBUF_NAMESPACE_ID::int64 value);

  // int64 length = 2;
  private:
  bool has_length() const;
  public:
  void clear_length();
  ::PROTOBUF_NAMESPACE_ID::int64 length() const;
  void set_length(::PROTOBUF_NAMESPACE_ID::int64 value);

  void clear_has_length();
  HasLengthCase has_length_case() const;
  // @@protoc_insertion_point(class_scope:tensorflow.TensorSliceProto.Extent)
 private:
  class _Internal;
  void set_has_length();

  inline bool has_has_length() const;
  inline void clear_has_has_length();

  ::PROTOBUF_NAMESPACE_ID::internal::InternalMetadataWithArena _internal_metadata_;
  template <typename T> friend class ::PROTOBUF_NAMESPACE_ID::Arena::InternalHelper;
  typedef void InternalArenaConstructable_;
  typedef void DestructorSkippable_;
  ::PROTOBUF_NAMESPACE_ID::int64 start_;
  union HasLengthUnion {
    HasLengthUnion() {}
    ::PROTOBUF_NAMESPACE_ID::int64 length_;
  } has_length_;
  mutable ::PROTOBUF_NAMESPACE_ID::internal::CachedSize _cached_size_;
  ::PROTOBUF_NAMESPACE_ID::uint32 _oneof_case_[1];

  friend struct ::TableStruct_tensorflow_2fcore_2fframework_2ftensor_5fslice_2eproto;
};
// -------------------------------------------------------------------

class TensorSliceProto :
    public ::PROTOBUF_NAMESPACE_ID::Message /* @@protoc_insertion_point(class_definition:tensorflow.TensorSliceProto) */ {
 public:
  TensorSliceProto();
  virtual ~TensorSliceProto();

  TensorSliceProto(const TensorSliceProto& from);
  TensorSliceProto(TensorSliceProto&& from) noexcept
    : TensorSliceProto() {
    *this = ::std::move(from);
  }

  inline TensorSliceProto& operator=(const TensorSliceProto& from) {
    CopyFrom(from);
    return *this;
  }
  inline TensorSliceProto& operator=(TensorSliceProto&& from) noexcept {
    if (GetArenaNoVirtual() == from.GetArenaNoVirtual()) {
      if (this != &from) InternalSwap(&from);
    } else {
      CopyFrom(from);
    }
    return *this;
  }

  inline ::PROTOBUF_NAMESPACE_ID::Arena* GetArena() const final {
    return GetArenaNoVirtual();
  }
  inline void* GetMaybeArenaPointer() const final {
    return MaybeArenaPtr();
  }
  static const ::PROTOBUF_NAMESPACE_ID::Descriptor* descriptor() {
    return GetDescriptor();
  }
  static const ::PROTOBUF_NAMESPACE_ID::Descriptor* GetDescriptor() {
    return GetMetadataStatic().descriptor;
  }
  static const ::PROTOBUF_NAMESPACE_ID::Reflection* GetReflection() {
    return GetMetadataStatic().reflection;
  }
  static const TensorSliceProto& default_instance();

  static void InitAsDefaultInstance();  // FOR INTERNAL USE ONLY
  static inline const TensorSliceProto* internal_default_instance() {
    return reinterpret_cast<const TensorSliceProto*>(
               &_TensorSliceProto_default_instance_);
  }
  static constexpr int kIndexInFileMessages =
    1;

  friend void swap(TensorSliceProto& a, TensorSliceProto& b) {
    a.Swap(&b);
  }
  inline void Swap(TensorSliceProto* other) {
    if (other == this) return;
    if (GetArenaNoVirtual() == other->GetArenaNoVirtual()) {
      InternalSwap(other);
    } else {
      ::PROTOBUF_NAMESPACE_ID::internal::GenericSwap(this, other);
    }
  }
  void UnsafeArenaSwap(TensorSliceProto* other) {
    if (other == this) return;
    GOOGLE_DCHECK(GetArenaNoVirtual() == other->GetArenaNoVirtual());
    InternalSwap(other);
  }

  // implements Message ----------------------------------------------

  inline TensorSliceProto* New() const final {
    return CreateMaybeMessage<TensorSliceProto>(nullptr);
  }

  TensorSliceProto* New(::PROTOBUF_NAMESPACE_ID::Arena* arena) const final {
    return CreateMaybeMessage<TensorSliceProto>(arena);
  }
  void CopyFrom(const ::PROTOBUF_NAMESPACE_ID::Message& from) final;
  void MergeFrom(const ::PROTOBUF_NAMESPACE_ID::Message& from) final;
  void CopyFrom(const TensorSliceProto& from);
  void MergeFrom(const TensorSliceProto& from);
  PROTOBUF_ATTRIBUTE_REINITIALIZES void Clear() final;
  bool IsInitialized() const final;

  size_t ByteSizeLong() const final;
  #if GOOGLE_PROTOBUF_ENABLE_EXPERIMENTAL_PARSER
  const char* _InternalParse(const char* ptr, ::PROTOBUF_NAMESPACE_ID::internal::ParseContext* ctx) final;
  #else
  bool MergePartialFromCodedStream(
      ::PROTOBUF_NAMESPACE_ID::io::CodedInputStream* input) final;
  #endif  // GOOGLE_PROTOBUF_ENABLE_EXPERIMENTAL_PARSER
  void SerializeWithCachedSizes(
      ::PROTOBUF_NAMESPACE_ID::io::CodedOutputStream* output) const final;
  ::PROTOBUF_NAMESPACE_ID::uint8* InternalSerializeWithCachedSizesToArray(
      ::PROTOBUF_NAMESPACE_ID::uint8* target) const final;
  int GetCachedSize() const final { return _cached_size_.Get(); }

  private:
  inline void SharedCtor();
  inline void SharedDtor();
  void SetCachedSize(int size) const final;
  void InternalSwap(TensorSliceProto* other);
  friend class ::PROTOBUF_NAMESPACE_ID::internal::AnyMetadata;
  static ::PROTOBUF_NAMESPACE_ID::StringPiece FullMessageName() {
    return "tensorflow.TensorSliceProto";
  }
  protected:
  explicit TensorSliceProto(::PROTOBUF_NAMESPACE_ID::Arena* arena);
  private:
  static void ArenaDtor(void* object);
  inline void RegisterArenaDtor(::PROTOBUF_NAMESPACE_ID::Arena* arena);
  private:
  inline ::PROTOBUF_NAMESPACE_ID::Arena* GetArenaNoVirtual() const {
    return _internal_metadata_.arena();
  }
  inline void* MaybeArenaPtr() const {
    return _internal_metadata_.raw_arena_ptr();
  }
  public:

  ::PROTOBUF_NAMESPACE_ID::Metadata GetMetadata() const final;
  private:
  static ::PROTOBUF_NAMESPACE_ID::Metadata GetMetadataStatic() {
    ::PROTOBUF_NAMESPACE_ID::internal::AssignDescriptors(&::descriptor_table_tensorflow_2fcore_2fframework_2ftensor_5fslice_2eproto);
    return ::descriptor_table_tensorflow_2fcore_2fframework_2ftensor_5fslice_2eproto.file_level_metadata[kIndexInFileMessages];
  }

  public:

  // nested types ----------------------------------------------------

  typedef TensorSliceProto_Extent Extent;

  // accessors -------------------------------------------------------

  enum : int {
    kExtentFieldNumber = 1,
  };
  // repeated .tensorflow.TensorSliceProto.Extent extent = 1;
  int extent_size() const;
  void clear_extent();
  ::tensorflow::TensorSliceProto_Extent* mutable_extent(int index);
  ::PROTOBUF_NAMESPACE_ID::RepeatedPtrField< ::tensorflow::TensorSliceProto_Extent >*
      mutable_extent();
  const ::tensorflow::TensorSliceProto_Extent& extent(int index) const;
  ::tensorflow::TensorSliceProto_Extent* add_extent();
  const ::PROTOBUF_NAMESPACE_ID::RepeatedPtrField< ::tensorflow::TensorSliceProto_Extent >&
      extent() const;

  // @@protoc_insertion_point(class_scope:tensorflow.TensorSliceProto)
 private:
  class _Internal;

  ::PROTOBUF_NAMESPACE_ID::internal::InternalMetadataWithArena _internal_metadata_;
  template <typename T> friend class ::PROTOBUF_NAMESPACE_ID::Arena::InternalHelper;
  typedef void InternalArenaConstructable_;
  typedef void DestructorSkippable_;
  ::PROTOBUF_NAMESPACE_ID::RepeatedPtrField< ::tensorflow::TensorSliceProto_Extent > extent_;
  mutable ::PROTOBUF_NAMESPACE_ID::internal::CachedSize _cached_size_;
  friend struct ::TableStruct_tensorflow_2fcore_2fframework_2ftensor_5fslice_2eproto;
};
// ===================================================================


// ===================================================================

#ifdef __GNUC__
  #pragma GCC diagnostic push
  #pragma GCC diagnostic ignored "-Wstrict-aliasing"
#endif  // __GNUC__
// TensorSliceProto_Extent

// int64 start = 1;
inline void TensorSliceProto_Extent::clear_start() {
  start_ = PROTOBUF_LONGLONG(0);
}
inline ::PROTOBUF_NAMESPACE_ID::int64 TensorSliceProto_Extent::start() const {
  // @@protoc_insertion_point(field_get:tensorflow.TensorSliceProto.Extent.start)
  return start_;
}
inline void TensorSliceProto_Extent::set_start(::PROTOBUF_NAMESPACE_ID::int64 value) {
  
  start_ = value;
  // @@protoc_insertion_point(field_set:tensorflow.TensorSliceProto.Extent.start)
}

// int64 length = 2;
inline bool TensorSliceProto_Extent::has_length() const {
  return has_length_case() == kLength;
}
inline void TensorSliceProto_Extent::set_has_length() {
  _oneof_case_[0] = kLength;
}
inline void TensorSliceProto_Extent::clear_length() {
  if (has_length()) {
    has_length_.length_ = PROTOBUF_LONGLONG(0);
    clear_has_has_length();
  }
}
inline ::PROTOBUF_NAMESPACE_ID::int64 TensorSliceProto_Extent::length() const {
  // @@protoc_insertion_point(field_get:tensorflow.TensorSliceProto.Extent.length)
  if (has_length()) {
    return has_length_.length_;
  }
  return PROTOBUF_LONGLONG(0);
}
inline void TensorSliceProto_Extent::set_length(::PROTOBUF_NAMESPACE_ID::int64 value) {
  if (!has_length()) {
    clear_has_length();
    set_has_length();
  }
  has_length_.length_ = value;
  // @@protoc_insertion_point(field_set:tensorflow.TensorSliceProto.Extent.length)
}

inline bool TensorSliceProto_Extent::has_has_length() const {
  return has_length_case() != HAS_LENGTH_NOT_SET;
}
inline void TensorSliceProto_Extent::clear_has_has_length() {
  _oneof_case_[0] = HAS_LENGTH_NOT_SET;
}
inline TensorSliceProto_Extent::HasLengthCase TensorSliceProto_Extent::has_length_case() const {
  return TensorSliceProto_Extent::HasLengthCase(_oneof_case_[0]);
}
// -------------------------------------------------------------------

// TensorSliceProto

// repeated .tensorflow.TensorSliceProto.Extent extent = 1;
inline int TensorSliceProto::extent_size() const {
  return extent_.size();
}
inline void TensorSliceProto::clear_extent() {
  extent_.Clear();
}
inline ::tensorflow::TensorSliceProto_Extent* TensorSliceProto::mutable_extent(int index) {
  // @@protoc_insertion_point(field_mutable:tensorflow.TensorSliceProto.extent)
  return extent_.Mutable(index);
}
inline ::PROTOBUF_NAMESPACE_ID::RepeatedPtrField< ::tensorflow::TensorSliceProto_Extent >*
TensorSliceProto::mutable_extent() {
  // @@protoc_insertion_point(field_mutable_list:tensorflow.TensorSliceProto.extent)
  return &extent_;
}
inline const ::tensorflow::TensorSliceProto_Extent& TensorSliceProto::extent(int index) const {
  // @@protoc_insertion_point(field_get:tensorflow.TensorSliceProto.extent)
  return extent_.Get(index);
}
inline ::tensorflow::TensorSliceProto_Extent* TensorSliceProto::add_extent() {
  // @@protoc_insertion_point(field_add:tensorflow.TensorSliceProto.extent)
  return extent_.Add();
}
inline const ::PROTOBUF_NAMESPACE_ID::RepeatedPtrField< ::tensorflow::TensorSliceProto_Extent >&
TensorSliceProto::extent() const {
  // @@protoc_insertion_point(field_list:tensorflow.TensorSliceProto.extent)
  return extent_;
}

#ifdef __GNUC__
  #pragma GCC diagnostic pop
#endif  // __GNUC__
// -------------------------------------------------------------------


// @@protoc_insertion_point(namespace_scope)

}  // namespace tensorflow

// @@protoc_insertion_point(global_scope)

#include <google/protobuf/port_undef.inc>
#endif  // GOOGLE_PROTOBUF_INCLUDED_GOOGLE_PROTOBUF_INCLUDED_tensorflow_2fcore_2fframework_2ftensor_5fslice_2eproto
