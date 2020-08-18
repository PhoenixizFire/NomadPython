/*===- TableGen'erated file -------------------------------------*- C++ -*-===*\
|*                                                                            *|
|* Dialect Declarations                                                       *|
|*                                                                            *|
|* Automatically generated file, do not edit!                                 *|
|*                                                                            *|
\*===----------------------------------------------------------------------===*/


class SPIRVDialect : public ::mlir::Dialect {
public:
  explicit SPIRVDialect(::mlir::MLIRContext *context);
  static ::llvm::StringRef getDialectNamespace() { return "spv"; }

  /// Parse an attribute registered to this dialect.
  ::mlir::Attribute parseAttribute(::mlir::DialectAsmParser &parser,
                                   ::mlir::Type type) const override;

  /// Print an attribute registered to this dialect.
  void printAttribute(::mlir::Attribute attr,
                      ::mlir::DialectAsmPrinter &os) const override;

  /// Parse a type registered to this dialect.
  ::mlir::Type parseType(::mlir::DialectAsmParser &parser) const override;

  /// Print a type registered to this dialect.
  void printType(::mlir::Type type,
                 ::mlir::DialectAsmPrinter &os) const override;

  /// Materialize a single constant operation from a given attribute value with
  /// the desired resultant type.
  ::mlir::Operation *materializeConstant(::mlir::OpBuilder &builder,
                                         ::mlir::Attribute value,
                                         ::mlir::Type type,
                                         ::mlir::Location loc) override;

    /// Provides a hook for verifying dialect attributes attached to the given
    /// op.
    ::mlir::LogicalResult verifyOperationAttribute(
        ::mlir::Operation *op, ::mlir::NamedAttribute attribute) override;

    /// Provides a hook for verifying dialect attributes attached to the given
    /// op's region argument.
    ::mlir::LogicalResult verifyRegionArgAttribute(
        ::mlir::Operation *op, unsigned regionIndex, unsigned argIndex,
        ::mlir::NamedAttribute attribute) override;

    /// Provides a hook for verifying dialect attributes attached to the given
    /// op's region result.
    ::mlir::LogicalResult verifyRegionResultAttribute(
        ::mlir::Operation *op, unsigned regionIndex, unsigned resultIndex,
        ::mlir::NamedAttribute attribute) override;

    //===------------------------------------------------------------------===//
    // Attribute
    //===------------------------------------------------------------------===//

    /// Returns the attribute name to use when specifying decorations on results
    /// of operations.
    static std::string getAttributeName(Decoration decoration);
  };