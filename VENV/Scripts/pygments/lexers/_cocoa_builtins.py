# -*- coding: utf-8 -*-
"""
    pygments.lexers._cocoa_builtins
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This file defines a set of types used across Cocoa frameworks from Apple.
    There is a list of @interfaces, @protocols and some other (structs, unions)

    File may be also used as standalone generator for aboves.

    :copyright: Copyright 2006-2019 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

COCOA_INTERFACES = {'UITableViewCell', 'HKCorrelationQuery', 'NSURLSessionDataTask', 'PHFetchOptions', 'NSLinguisticTagger', 'NSStream', 'AVAudioUnitDelay', 'GCMotion', 'SKPhysicsWorld', 'NSString', 'CMAttitude', 'AVAudioEnvironmentDistanceAttenuationParameters', 'HKStatisticsCollection', 'SCNPlane', 'CBPeer', 'JSContext', 'SCNTransaction', 'SCNTorus', 'AVAudioUnitEffect', 'UICollectionReusableView', 'MTLSamplerDescriptor', 'AVAssetReaderSampleReferenceOutput', 'AVMutableCompositionTrack', 'GKLeaderboard', 'NSFetchedResultsController', 'SKRange', 'MKTileOverlayRenderer', 'MIDINetworkSession', 'UIVisualEffectView', 'CIWarpKernel', 'PKObject', 'MKRoute', 'MPVolumeView', 'UIPrintInfo', 'SCNText', 'ADClient', 'PKPayment', 'AVMutableAudioMix', 'GLKEffectPropertyLight', 'WKScriptMessage', 'AVMIDIPlayer', 'PHCollectionListChangeRequest', 'UICollectionViewLayout', 'NSMutableCharacterSet', 'SKPaymentTransaction', 'NEOnDemandRuleConnect', 'NSShadow', 'SCNView', 'NSURLSessionConfiguration', 'MTLVertexAttributeDescriptor', 'CBCharacteristic', 'HKQuantityType', 'CKLocationSortDescriptor', 'NEVPNIKEv2SecurityAssociationParameters', 'CMStepCounter', 'NSNetService', 'AVAssetWriterInputMetadataAdaptor', 'UICollectionView', 'UIViewPrintFormatter', 'SCNLevelOfDetail', 'CAShapeLayer', 'MCPeerID', 'MPRatingCommand', 'WKNavigation', 'NSDictionary', 'NSFileVersion', 'CMGyroData', 'AVAudioUnitDistortion', 'CKFetchRecordsOperation', 'SKPhysicsJointSpring', 'SCNHitTestResult', 'AVAudioTime', 'CIFilter', 'UIView', 'SCNConstraint', 'CAPropertyAnimation', 'MKMapItem', 'MPRemoteCommandCenter', 'PKPaymentSummaryItem', 'UICollectionViewFlowLayoutInvalidationContext', 'UIInputViewController', 'PKPass', 'SCNPhysicsBehavior', 'MTLRenderPassColorAttachmentDescriptor', 'MKPolygonRenderer', 'CKNotification', 'JSValue', 'PHCollectionList', 'CLGeocoder', 'NSByteCountFormatter', 'AVCaptureScreenInput', 'MPFeedbackCommand', 'CAAnimation', 'MKOverlayPathView', 'UIActionSheet', 'UIMotionEffectGroup', 'NSLengthFormatter', 'UIBarItem', 'SKProduct', 'AVAssetExportSession', 'NSKeyedUnarchiver', 'NSMutableSet', 'SCNPyramid', 'PHAssetCollection', 'MKMapView', 'HMHomeManager', 'CATransition', 'MTLCompileOptions', 'UIVibrancyEffect', 'CLCircularRegion', 'MKTileOverlay', 'SCNShape', 'ACAccountCredential', 'SKPhysicsJointLimit', 'MKMapSnapshotter', 'AVMediaSelectionGroup', 'NSIndexSet', 'CBPeripheralManager', 'CKRecordZone', 'AVAudioRecorder', 'NSURL', 'CBCentral', 'NSNumber', 'AVAudioOutputNode', 'MTLVertexAttributeDescriptorArray', 'MKETAResponse', 'SKTransition', 'SSReadingList', 'HKSourceQuery', 'UITableViewRowAction', 'UITableView', 'SCNParticlePropertyController', 'AVCaptureStillImageOutput', 'GCController', 'AVAudioPlayerNode', 'AVAudioSessionPortDescription', 'NSHTTPURLResponse', 'NEOnDemandRuleEvaluateConnection', 'SKEffectNode', 'HKQuantity', 'GCControllerElement', 'AVPlayerItemAccessLogEvent', 'SCNBox', 'NSExtensionContext', 'MKOverlayRenderer', 'SCNPhysicsVehicle', 'NSDecimalNumber', 'EKReminder', 'MKPolylineView', 'CKQuery', 'AVAudioMixerNode', 'GKAchievementDescription', 'EKParticipant', 'NSBlockOperation', 'UIActivityItemProvider', 'CLLocation', 'NSBatchUpdateRequest', 'PHContentEditingOutput', 'PHObjectChangeDetails', 'HKWorkoutType', 'MPMoviePlayerController', 'AVAudioFormat', 'HMTrigger', 'MTLRenderPassDepthAttachmentDescriptor', 'SCNRenderer', 'GKScore', 'UISplitViewController', 'HKSource', 'NSURLConnection', 'ABUnknownPersonViewController', 'SCNTechnique', 'UIMenuController', 'NSEvent', 'SKTextureAtlas', 'NSKeyedArchiver', 'GKLeaderboardSet', 'NSSimpleCString', 'AVAudioPCMBuffer', 'CBATTRequest', 'GKMatchRequest', 'AVMetadataObject', 'SKProductsRequest', 'UIAlertView', 'NSIncrementalStore', 'MFMailComposeViewController', 'SCNFloor', 'NSSortDescriptor', 'CKFetchNotificationChangesOperation', 'MPMovieAccessLog', 'NSManagedObjectContext', 'AVAudioUnitGenerator', 'WKBackForwardList', 'SKMutableTexture', 'AVCaptureAudioDataOutput', 'ACAccount', 'AVMetadataItem', 'MPRatingCommandEvent', 'AVCaptureDeviceInputSource', 'CLLocationManager', 'MPRemoteCommand', 'AVCaptureSession', 'UIStepper', 'UIRefreshControl', 'NEEvaluateConnectionRule', 'CKModifyRecordsOperation', 'UICollectionViewTransitionLayout', 'CBCentralManager', 'NSPurgeableData', 'PKShippingMethod', 'SLComposeViewController', 'NSHashTable', 'MKUserTrackingBarButtonItem', 'UILexiconEntry', 'CMMotionActivity', 'SKAction', 'SKShader', 'AVPlayerItemOutput', 'MTLRenderPassAttachmentDescriptor', 'UIDocumentInteractionController', 'UIDynamicItemBehavior', 'NSMutableDictionary', 'UILabel', 'AVCaptureInputPort', 'NSExpression', 'CAInterAppAudioTransportView', 'SKMutablePayment', 'UIImage', 'PHCachingImageManager', 'SCNTransformConstraint', 'HKCorrelationType', 'UIColor', 'SCNGeometrySource', 'AVCaptureAutoExposureBracketedStillImageSettings', 'UIPopoverBackgroundView', 'UIToolbar', 'NSNotificationCenter', 'UICollectionViewLayoutAttributes', 'AVAssetReaderOutputMetadataAdaptor', 'NSEntityMigrationPolicy', 'HMUser', 'NSLocale', 'NSURLSession', 'SCNCamera', 'NSTimeZone', 'UIManagedDocument', 'AVMutableVideoCompositionLayerInstruction', 'AVAssetTrackGroup', 'NSInvocationOperation', 'ALAssetRepresentation', 'AVQueuePlayer', 'HMServiceGroup', 'UIPasteboard', 'PHContentEditingInput', 'NSLayoutManager', 'EKCalendarChooser', 'EKObject', 'CATiledLayer', 'GLKReflectionMapEffect', 'NSManagedObjectID', 'NSEnergyFormatter', 'SLRequest', 'HMCharacteristic', 'AVPlayerLayer', 'MTLRenderPassDescriptor', 'SKPayment', 'NSPointerArray', 'AVAudioMix', 'SCNLight', 'MCAdvertiserAssistant', 'MKMapSnapshotOptions', 'HKCategorySample', 'AVAudioEnvironmentReverbParameters', 'SCNMorpher', 'AVTimedMetadataGroup', 'CBMutableCharacteristic', 'NSFetchRequest', 'UIDevice', 'NSManagedObject', 'NKAssetDownload', 'AVOutputSettingsAssistant', 'SKPhysicsJointPin', 'UITabBar', 'UITextInputMode', 'NSFetchRequestExpression', 'HMActionSet', 'CTSubscriber', 'PHAssetChangeRequest', 'NSPersistentStoreRequest', 'UITabBarController', 'HKQuantitySample', 'AVPlayerItem', 'AVSynchronizedLayer', 'MKDirectionsRequest', 'NSMetadataItem', 'UIPresentationController', 'UINavigationItem', 'PHFetchResultChangeDetails', 'PHImageManager', 'AVCaptureManualExposureBracketedStillImageSettings', 'UIStoryboardPopoverSegue', 'SCNLookAtConstraint', 'UIGravityBehavior', 'UIWindow', 'CBMutableDescriptor', 'NEOnDemandRuleDisconnect', 'UIBezierPath', 'UINavigationController', 'ABPeoplePickerNavigationController', 'EKSource', 'AVAssetWriterInput', 'AVPlayerItemTrack', 'GLKEffectPropertyTexture', 'NSHTTPCookie', 'NSURLResponse', 'SKPaymentQueue', 'NSAssertionHandler', 'MKReverseGeocoder', 'GCControllerAxisInput', 'NSArray', 'NSOrthography', 'NSURLSessionUploadTask', 'NSCharacterSet', 'AVMutableVideoCompositionInstruction', 'AVAssetReaderOutput', 'EAGLContext', 'WKFrameInfo', 'CMPedometer', 'MyClass', 'CKModifyBadgeOperation', 'AVCaptureAudioFileOutput', 'SKEmitterNode', 'NSMachPort', 'AVVideoCompositionCoreAnimationTool', 'PHCollection', 'SCNPhysicsWorld', 'NSURLRequest', 'CMAccelerometerData', 'NSNetServiceBrowser', 'CLFloor', 'AVAsynchronousVideoCompositionRequest', 'SCNGeometry', 'SCNIKConstraint', 'CIKernel', 'CAGradientLayer', 'HKCharacteristicType', 'NSFormatter', 'SCNAction', 'CATransaction', 'CBUUID', 'UIStoryboard', 'MPMediaLibrary', 'UITapGestureRecognizer', 'MPMediaItemArtwork', 'NSURLSessionTask', 'AVAudioUnit', 'MCBrowserViewController', 'UIFontDescriptor', 'NSRelationshipDescription', 'HKSample', 'WKWebView', 'NSMutableAttributedString', 'NSPersistentStoreAsynchronousResult', 'MPNowPlayingInfoCenter', 'MKLocalSearch', 'EAAccessory', 'HKCorrelation', 'CATextLayer', 'NSNotificationQueue', 'UINib', 'GLKTextureLoader', 'HKObjectType', 'NSValue', 'NSMutableIndexSet', 'SKPhysicsContact', 'NSProgress', 'AVPlayerViewController', 'CAScrollLayer', 'GKSavedGame', 'NSTextCheckingResult', 'PHObjectPlaceholder', 'SKConstraint', 'EKEventEditViewController', 'NSEntityDescription', 'NSURLCredentialStorage', 'UIApplication', 'SKDownload', 'SCNNode', 'MKLocalSearchRequest', 'SKScene', 'UISearchDisplayController', 'NEOnDemandRule', 'MTLRenderPassStencilAttachmentDescriptor', 'CAReplicatorLayer', 'UIPrintPageRenderer', 'EKCalendarItem', 'NSUUID', 'EAAccessoryManager', 'NEOnDemandRuleIgnore', 'SKRegion', 'AVAssetResourceLoader', 'EAWiFiUnconfiguredAccessoryBrowser', 'NSUserActivity', 'CTCall', 'UIPrinterPickerController', 'CIVector', 'UINavigationBar', 'UIPanGestureRecognizer', 'MPMediaQuery', 'ABNewPersonViewController', 'CKRecordZoneID', 'HKAnchoredObjectQuery', 'CKFetchRecordZonesOperation', 'UIStoryboardSegue', 'ACAccountType', 'GKSession', 'SKVideoNode', 'PHChange', 'SKReceiptRefreshRequest', 'GCExtendedGamepadSnapshot', 'MPSeekCommandEvent', 'GCExtendedGamepad', 'CAValueFunction', 'SCNCylinder', 'NSNotification', 'NSBatchUpdateResult', 'PKPushCredentials', 'SCNPhysicsSliderJoint', 'AVCaptureDeviceFormat', 'AVPlayerItemErrorLog', 'NSMapTable', 'NSSet', 'CMMotionManager', 'GKVoiceChatService', 'UIPageControl', 'UILexicon', 'MTLArrayType', 'AVAudioUnitReverb', 'MKGeodesicPolyline', 'AVMutableComposition', 'NSLayoutConstraint', 'UIPrinter', 'NSOrderedSet', 'CBAttribute', 'PKPushPayload', 'NSIncrementalStoreNode', 'EKEventStore', 'MPRemoteCommandEvent', 'UISlider', 'UIBlurEffect', 'CKAsset', 'AVCaptureInput', 'AVAudioEngine', 'MTLVertexDescriptor', 'SKPhysicsBody', 'NSOperation', 'PKPaymentPass', 'UIImageAsset', 'MKMapCamera', 'SKProductsResponse', 'GLKEffectPropertyMaterial', 'AVCaptureDevice', 'CTCallCenter', 'CABTMIDILocalPeripheralViewController', 'NEVPNManager', 'HKQuery', 'SCNPhysicsContact', 'CBMutableService', 'AVSampleBufferDisplayLayer', 'SCNSceneSource', 'SKLightNode', 'CKDiscoveredUserInfo', 'NSMutableArray', 'MTLDepthStencilDescriptor', 'MTLArgument', 'NSMassFormatter', 'CIRectangleFeature', 'PKPushRegistry', 'NEVPNConnection', 'MCNearbyServiceBrowser', 'NSOperationQueue', 'MKPolylineRenderer', 'HKWorkout', 'NSValueTransformer', 'UICollectionViewFlowLayout', 'MPChangePlaybackRateCommandEvent', 'NSEntityMapping', 'SKTexture', 'NSMergePolicy', 'UITextInputStringTokenizer', 'NSRecursiveLock', 'AVAsset', 'NSUndoManager', 'AVAudioUnitSampler', 'NSItemProvider', 'SKUniform', 'MPMediaPickerController', 'CKOperation', 'MTLRenderPipelineDescriptor', 'EAWiFiUnconfiguredAccessory', 'NSFileCoordinator', 'SKRequest', 'NSFileHandle', 'NSConditionLock', 'UISegmentedControl', 'NSManagedObjectModel', 'UITabBarItem', 'SCNCone', 'MPMediaItem', 'SCNMaterial', 'EKRecurrenceRule', 'UIEvent', 'UITouch', 'UIPrintInteractionController', 'CMDeviceMotion', 'NEVPNProtocol', 'NSCompoundPredicate', 'HKHealthStore', 'MKMultiPoint', 'HKSampleType', 'UIPrintFormatter', 'AVAudioUnitEQFilterParameters', 'SKView', 'NSConstantString', 'UIPopoverController', 'CKDatabase', 'AVMetadataFaceObject', 'UIAccelerometer', 'EKEventViewController', 'CMAltitudeData', 'MTLStencilDescriptor', 'UISwipeGestureRecognizer', 'NSPort', 'MKCircleRenderer', 'AVCompositionTrack', 'NSAsynchronousFetchRequest', 'NSUbiquitousKeyValueStore', 'NSMetadataQueryResultGroup', 'AVAssetResourceLoadingDataRequest', 'UITableViewHeaderFooterView', 'CKNotificationID', 'AVAudioSession', 'HKUnit', 'NSNull', 'NSPersistentStoreResult', 'MKCircleView', 'AVAudioChannelLayout', 'NEVPNProtocolIKEv2', 'WKProcessPool', 'UIAttachmentBehavior', 'CLBeacon', 'NSInputStream', 'NSURLCache', 'GKPlayer', 'NSMappingModel', 'CIQRCodeFeature', 'AVMutableVideoComposition', 'PHFetchResult', 'NSAttributeDescription', 'AVPlayer', 'MKAnnotationView', 'PKPaymentRequest', 'NSTimer', 'CBDescriptor', 'MKOverlayView', 'AVAudioUnitTimePitch', 'NSSaveChangesRequest', 'UIReferenceLibraryViewController', 'SKPhysicsJointFixed', 'UILocalizedIndexedCollation', 'UIInterpolatingMotionEffect', 'UIDocumentPickerViewController', 'AVAssetWriter', 'NSBundle', 'SKStoreProductViewController', 'GLKViewController', 'NSMetadataQueryAttributeValueTuple', 'GKTurnBasedMatch', 'AVAudioFile', 'UIActivity', 'NSPipe', 'MKShape', 'NSMergeConflict', 'CIImage', 'HKObject', 'UIRotationGestureRecognizer', 'AVPlayerItemLegibleOutput', 'AVAssetImageGenerator', 'GCControllerButtonInput', 'CKMarkNotificationsReadOperation', 'CKSubscription', 'MPTimedMetadata', 'NKIssue', 'UIScreenMode', 'HMAccessoryBrowser', 'GKTurnBasedEventHandler', 'UIWebView', 'MKPolyline', 'JSVirtualMachine', 'AVAssetReader', 'NSAttributedString', 'GKMatchmakerViewController', 'NSCountedSet', 'UIButton', 'WKNavigationResponse', 'GKLocalPlayer', 'MPMovieErrorLog', 'AVSpeechUtterance', 'HKStatistics', 'UILocalNotification', 'HKBiologicalSexObject', 'AVURLAsset', 'CBPeripheral', 'NSDateComponentsFormatter', 'SKSpriteNode', 'UIAccessibilityElement', 'AVAssetWriterInputGroup', 'HMZone', 'AVAssetReaderAudioMixOutput', 'NSEnumerator', 'UIDocument', 'MKLocalSearchResponse', 'UISimpleTextPrintFormatter', 'PHPhotoLibrary', 'CBService', 'UIDocumentMenuViewController', 'MCSession', 'QLPreviewController', 'CAMediaTimingFunction', 'UITextPosition', 'ASIdentifierManager', 'AVAssetResourceLoadingRequest', 'SLComposeServiceViewController', 'UIPinchGestureRecognizer', 'PHObject', 'NSExtensionItem', 'HKSampleQuery', 'MTLRenderPipelineColorAttachmentDescriptorArray', 'MKRouteStep', 'SCNCapsule', 'NSMetadataQuery', 'AVAssetResourceLoadingContentInformationRequest', 'UITraitCollection', 'CTCarrier', 'NSFileSecurity', 'UIAcceleration', 'UIMotionEffect', 'MTLRenderPipelineReflection', 'CLHeading', 'CLVisit', 'MKDirectionsResponse', 'HMAccessory', 'MTLStructType', 'UITextView', 'CMMagnetometerData', 'UICollisionBehavior', 'UIProgressView', 'CKServerChangeToken', 'UISearchBar', 'MKPlacemark', 'AVCaptureConnection', 'NSPropertyMapping', 'ALAssetsFilter', 'SK3DNode', 'AVPlayerItemErrorLogEvent', 'NSJSONSerialization', 'AVAssetReaderVideoCompositionOutput', 'ABPersonViewController', 'CIDetector', 'GKTurnBasedMatchmakerViewController', 'MPMediaItemCollection', 'SCNSphere', 'NSCondition', 'NSURLCredential', 'MIDINetworkConnection', 'NSFileProviderExtension', 'NSDecimalNumberHandler', 'NSAtomicStoreCacheNode', 'NSAtomicStore', 'EKAlarm', 'CKNotificationInfo', 'AVAudioUnitEQ', 'UIPercentDrivenInteractiveTransition', 'MKPolygon', 'AVAssetTrackSegment', 'MTLVertexAttribute', 'NSExpressionDescription', 'HKStatisticsCollectionQuery', 'NSURLAuthenticationChallenge', 'NSDirectoryEnumerator', 'MKDistanceFormatter', 'UIAlertAction', 'NSPropertyListSerialization', 'GKPeerPickerController', 'UIUserNotificationSettings', 'UITableViewController', 'GKNotificationBanner', 'MKPointAnnotation', 'MTLRenderPassColorAttachmentDescriptorArray', 'NSCache', 'SKPhysicsJoint', 'NSXMLParser', 'UIViewController', 'PKPaymentToken', 'MFMessageComposeViewController', 'AVAudioInputNode', 'NSDataDetector', 'CABTMIDICentralViewController', 'AVAudioUnitMIDIInstrument', 'AVCaptureVideoPreviewLayer', 'AVAssetWriterInputPassDescription', 'MPChangePlaybackRateCommand', 'NSURLComponents', 'CAMetalLayer', 'UISnapBehavior', 'AVMetadataMachineReadableCodeObject', 'CKDiscoverUserInfosOperation', 'NSTextAttachment', 'NSException', 'UIMenuItem', 'CMMotionActivityManager', 'SCNGeometryElement', 'NCWidgetController', 'CAEmitterLayer', 'MKUserLocation', 'UIImagePickerController', 'CIFeature', 'AVCaptureDeviceInput', 'ALAsset', 'NSURLSessionDownloadTask', 'SCNPhysicsHingeJoint', 'MPMoviePlayerViewController', 'NSMutableOrderedSet', 'SCNMaterialProperty', 'UIFont', 'AVCaptureVideoDataOutput', 'NSCachedURLResponse', 'ALAssetsLibrary', 'NSInvocation', 'UILongPressGestureRecognizer', 'NSTextStorage', 'WKWebViewConfiguration', 'CIFaceFeature', 'MKMapSnapshot', 'GLKEffectPropertyFog', 'AVComposition', 'CKDiscoverAllContactsOperation', 'AVAudioMixInputParameters', 'CAEmitterBehavior', 'PKPassLibrary', 'UIMutableUserNotificationCategory', 'NSLock', 'NEVPNProtocolIPSec', 'ADBannerView', 'UIDocumentPickerExtensionViewController', 'UIActivityIndicatorView', 'AVPlayerMediaSelectionCriteria', 'CALayer', 'UIAccessibilityCustomAction', 'UIBarButtonItem', 'AVAudioSessionRouteDescription', 'CLBeaconRegion', 'HKBloodTypeObject', 'MTLVertexBufferLayoutDescriptorArray', 'CABasicAnimation', 'AVVideoCompositionInstruction', 'AVMutableTimedMetadataGroup', 'EKRecurrenceEnd', 'NSTextContainer', 'TWTweetComposeViewController', 'PKPaymentAuthorizationViewController', 'UIScrollView', 'WKNavigationAction', 'AVPlayerItemMetadataOutput', 'EKRecurrenceDayOfWeek', 'NSNumberFormatter', 'MTLComputePipelineReflection', 'UIScreen', 'CLRegion', 'NSProcessInfo', 'GLKTextureInfo', 'SCNSkinner', 'AVCaptureMetadataOutput', 'SCNAnimationEvent', 'NSTextTab', 'JSManagedValue', 'NSDate', 'UITextChecker', 'WKBackForwardListItem', 'NSData', 'NSParagraphStyle', 'AVMutableMetadataItem', 'EKCalendar', 'HKWorkoutEvent', 'NSMutableURLRequest', 'UIVideoEditorController', 'HMTimerTrigger', 'AVAudioUnitVarispeed', 'UIDynamicAnimator', 'AVCompositionTrackSegment', 'GCGamepadSnapshot', 'MPMediaEntity', 'GLKSkyboxEffect', 'UISwitch', 'EKStructuredLocation', 'UIGestureRecognizer', 'NSProxy', 'GLKBaseEffect', 'UIPushBehavior', 'GKScoreChallenge', 'NSCoder', 'MPMediaPlaylist', 'NSDateComponents', 'WKUserScript', 'EKEvent', 'NSDateFormatter', 'NSAsynchronousFetchResult', 'AVAssetWriterInputPixelBufferAdaptor', 'UIVisualEffect', 'UICollectionViewCell', 'UITextField', 'CLPlacemark', 'MPPlayableContentManager', 'AVCaptureOutput', 'HMCharacteristicWriteAction', 'CKModifySubscriptionsOperation', 'NSPropertyDescription', 'GCGamepad', 'UIMarkupTextPrintFormatter', 'SCNTube', 'NSPersistentStoreCoordinator', 'AVAudioEnvironmentNode', 'GKMatchmaker', 'CIContext', 'NSThread', 'SLComposeSheetConfigurationItem', 'SKPhysicsJointSliding', 'NSPredicate', 'GKVoiceChat', 'SKCropNode', 'AVCaptureAudioPreviewOutput', 'NSStringDrawingContext', 'GKGameCenterViewController', 'UIPrintPaper', 'SCNPhysicsBallSocketJoint', 'UICollectionViewLayoutInvalidationContext', 'GLKEffectPropertyTransform', 'AVAudioIONode', 'UIDatePicker', 'MKDirections', 'ALAssetsGroup', 'CKRecordZoneNotification', 'SCNScene', 'MPMovieAccessLogEvent', 'CKFetchSubscriptionsOperation', 'CAEmitterCell', 'AVAudioUnitTimeEffect', 'HMCharacteristicMetadata', 'MKPinAnnotationView', 'UIPickerView', 'UIImageView', 'UIUserNotificationCategory', 'SCNPhysicsVehicleWheel', 'HKCategoryType', 'MPMediaQuerySection', 'GKFriendRequestComposeViewController', 'NSError', 'MTLRenderPipelineColorAttachmentDescriptor', 'SCNPhysicsShape', 'UISearchController', 'SCNPhysicsBody', 'CTSubscriberInfo', 'AVPlayerItemAccessLog', 'MPMediaPropertyPredicate', 'CMLogItem', 'NSAutoreleasePool', 'NSSocketPort', 'AVAssetReaderTrackOutput', 'SKNode', 'UIMutableUserNotificationAction', 'SCNProgram', 'AVSpeechSynthesisVoice', 'CMAltimeter', 'AVCaptureAudioChannel', 'GKTurnBasedExchangeReply', 'AVVideoCompositionLayerInstruction', 'AVSpeechSynthesizer', 'GKChallengeEventHandler', 'AVCaptureFileOutput', 'UIControl', 'SCNPhysicsField', 'CKReference', 'LAContext', 'CKRecordID', 'ADInterstitialAd', 'AVAudioSessionDataSourceDescription', 'AVAudioBuffer', 'CIColorKernel', 'GCControllerDirectionPad', 'NSFileManager', 'AVMutableAudioMixInputParameters', 'UIScreenEdgePanGestureRecognizer', 'CAKeyframeAnimation', 'CKQueryNotification', 'PHAdjustmentData', 'EASession', 'AVAssetResourceRenewalRequest', 'UIInputView', 'NSFileWrapper', 'UIResponder', 'NSPointerFunctions', 'UIKeyCommand', 'NSHTTPCookieStorage', 'AVMediaSelectionOption', 'NSRunLoop', 'NSFileAccessIntent', 'CAAnimationGroup', 'MKCircle', 'UIAlertController', 'NSMigrationManager', 'NSDateIntervalFormatter', 'UICollectionViewUpdateItem', 'CKDatabaseOperation', 'PHImageRequestOptions', 'SKReachConstraints', 'CKRecord', 'CAInterAppAudioSwitcherView', 'WKWindowFeatures', 'GKInvite', 'NSMutableData', 'PHAssetCollectionChangeRequest', 'NSMutableParagraphStyle', 'UIDynamicBehavior', 'GLKEffectProperty', 'CKFetchRecordChangesOperation', 'SKShapeNode', 'MPMovieErrorLogEvent', 'MKPolygonView', 'MPContentItem', 'HMAction', 'NSScanner', 'GKAchievementChallenge', 'AVAudioPlayer', 'CKContainer', 'AVVideoComposition', 'NKLibrary', 'NSPersistentStore', 'AVCaptureMovieFileOutput', 'HMRoom', 'GKChallenge', 'UITextRange', 'NSURLProtectionSpace', 'ACAccountStore', 'MPSkipIntervalCommand', 'NSComparisonPredicate', 'HMHome', 'PHVideoRequestOptions', 'NSOutputStream', 'MPSkipIntervalCommandEvent', 'PKAddPassesViewController', 'UITextSelectionRect', 'CTTelephonyNetworkInfo', 'AVTextStyleRule', 'NSFetchedPropertyDescription', 'UIPageViewController', 'CATransformLayer', 'UICollectionViewController', 'AVAudioNode', 'MCNearbyServiceAdvertiser', 'NSObject', 'PHAsset', 'GKLeaderboardViewController', 'CKQueryCursor', 'MPMusicPlayerController', 'MKOverlayPathRenderer', 'CMPedometerData', 'HMService', 'SKFieldNode', 'GKAchievement', 'WKUserContentController', 'AVAssetTrack', 'TWRequest', 'SKLabelNode', 'AVCaptureBracketedStillImageSettings', 'MIDINetworkHost', 'MPMediaPredicate', 'AVFrameRateRange', 'MTLTextureDescriptor', 'MTLVertexBufferLayoutDescriptor', 'MPFeedbackCommandEvent', 'UIUserNotificationAction', 'HKStatisticsQuery', 'SCNParticleSystem', 'NSIndexPath', 'AVVideoCompositionRenderContext', 'CADisplayLink', 'HKObserverQuery', 'UIPopoverPresentationController', 'CKQueryOperation', 'CAEAGLLayer', 'NSMutableString', 'NSMessagePort', 'NSURLQueryItem', 'MTLStructMember', 'AVAudioSessionChannelDescription', 'GLKView', 'UIActivityViewController', 'GKAchievementViewController', 'GKTurnBasedParticipant', 'NSURLProtocol', 'NSUserDefaults', 'NSCalendar', 'SKKeyframeSequence', 'AVMetadataItemFilter', 'CKModifyRecordZonesOperation', 'WKPreferences', 'NSMethodSignature', 'NSRegularExpression', 'EAGLSharegroup', 'AVPlayerItemVideoOutput', 'PHContentEditingInputRequestOptions', 'GKMatch', 'CIColor', 'UIDictationPhrase'}
COCOA_PROTOCOLS = {'SKStoreProductViewControllerDelegate', 'AVVideoCompositionInstruction', 'AVAudioSessionDelegate', 'GKMatchDelegate', 'NSFileManagerDelegate', 'UILayoutSupport', 'NSCopying', 'UIPrintInteractionControllerDelegate', 'QLPreviewControllerDataSource', 'SKProductsRequestDelegate', 'NSTextStorageDelegate', 'MCBrowserViewControllerDelegate', 'MTLComputeCommandEncoder', 'SCNSceneExportDelegate', 'UISearchResultsUpdating', 'MFMailComposeViewControllerDelegate', 'MTLBlitCommandEncoder', 'NSDecimalNumberBehaviors', 'PHContentEditingController', 'NSMutableCopying', 'UIActionSheetDelegate', 'UIViewControllerTransitioningDelegate', 'UIAlertViewDelegate', 'AVAudioPlayerDelegate', 'MKReverseGeocoderDelegate', 'NSCoding', 'UITextInputTokenizer', 'GKFriendRequestComposeViewControllerDelegate', 'UIActivityItemSource', 'NSCacheDelegate', 'UIAdaptivePresentationControllerDelegate', 'GKAchievementViewControllerDelegate', 'UIViewControllerTransitionCoordinator', 'EKEventEditViewDelegate', 'NSURLConnectionDelegate', 'UITableViewDelegate', 'GKPeerPickerControllerDelegate', 'UIGuidedAccessRestrictionDelegate', 'AVSpeechSynthesizerDelegate', 'AVAudio3DMixing', 'AVPlayerItemLegibleOutputPushDelegate', 'ADInterstitialAdDelegate', 'HMAccessoryBrowserDelegate', 'AVAssetResourceLoaderDelegate', 'UITabBarControllerDelegate', 'CKRecordValue', 'SKPaymentTransactionObserver', 'AVCaptureAudioDataOutputSampleBufferDelegate', 'UIInputViewAudioFeedback', 'GKChallengeListener', 'SKSceneDelegate', 'UIPickerViewDelegate', 'UIWebViewDelegate', 'UIApplicationDelegate', 'GKInviteEventListener', 'MPMediaPlayback', 'MyClassJavaScriptMethods', 'AVAsynchronousKeyValueLoading', 'QLPreviewItem', 'SCNBoundingVolume', 'NSPortDelegate', 'UIContentContainer', 'SCNNodeRendererDelegate', 'SKRequestDelegate', 'SKPhysicsContactDelegate', 'HMAccessoryDelegate', 'UIPageViewControllerDataSource', 'SCNSceneRendererDelegate', 'SCNPhysicsContactDelegate', 'MKMapViewDelegate', 'AVPlayerItemOutputPushDelegate', 'UICollectionViewDelegate', 'UIImagePickerControllerDelegate', 'MTLRenderCommandEncoder', 'PKPaymentAuthorizationViewControllerDelegate', 'UIToolbarDelegate', 'WKUIDelegate', 'SCNActionable', 'NSURLConnectionDataDelegate', 'MKOverlay', 'CBCentralManagerDelegate', 'JSExport', 'NSTextLayoutOrientationProvider', 'UIPickerViewDataSource', 'PKPushRegistryDelegate', 'UIViewControllerTransitionCoordinatorContext', 'NSLayoutManagerDelegate', 'MTLLibrary', 'NSFetchedResultsControllerDelegate', 'ABPeoplePickerNavigationControllerDelegate', 'MTLResource', 'NSDiscardableContent', 'UITextFieldDelegate', 'MTLBuffer', 'MTLSamplerState', 'GKGameCenterControllerDelegate', 'MPMediaPickerControllerDelegate', 'UISplitViewControllerDelegate', 'UIAppearance', 'UIPickerViewAccessibilityDelegate', 'UITraitEnvironment', 'UIScrollViewAccessibilityDelegate', 'ADBannerViewDelegate', 'MPPlayableContentDataSource', 'MTLComputePipelineState', 'NSURLSessionDelegate', 'MTLCommandBuffer', 'NSXMLParserDelegate', 'UIViewControllerRestoration', 'UISearchBarDelegate', 'UIBarPositioning', 'CBPeripheralDelegate', 'UISearchDisplayDelegate', 'CAAction', 'PKAddPassesViewControllerDelegate', 'MCNearbyServiceAdvertiserDelegate', 'MTLDepthStencilState', 'GKTurnBasedMatchmakerViewControllerDelegate', 'MPPlayableContentDelegate', 'AVCaptureVideoDataOutputSampleBufferDelegate', 'UIAppearanceContainer', 'UIStateRestoring', 'UITextDocumentProxy', 'MTLDrawable', 'NSURLSessionTaskDelegate', 'NSFilePresenter', 'AVAudioStereoMixing', 'UIViewControllerContextTransitioning', 'UITextInput', 'CBPeripheralManagerDelegate', 'UITextInputDelegate', 'NSFastEnumeration', 'NSURLAuthenticationChallengeSender', 'SCNProgramDelegate', 'AVVideoCompositing', 'SCNAnimatable', 'NSSecureCoding', 'MCAdvertiserAssistantDelegate', 'GKLocalPlayerListener', 'GLKNamedEffect', 'UIPopoverControllerDelegate', 'AVCaptureMetadataOutputObjectsDelegate', 'NSExtensionRequestHandling', 'UITextSelecting', 'UIPrinterPickerControllerDelegate', 'NCWidgetProviding', 'MTLCommandEncoder', 'NSURLProtocolClient', 'MFMessageComposeViewControllerDelegate', 'UIVideoEditorControllerDelegate', 'WKNavigationDelegate', 'GKSavedGameListener', 'UITableViewDataSource', 'MTLFunction', 'EKCalendarChooserDelegate', 'NSUserActivityDelegate', 'UICollisionBehaviorDelegate', 'NSStreamDelegate', 'MCNearbyServiceBrowserDelegate', 'HMHomeDelegate', 'UINavigationControllerDelegate', 'MCSessionDelegate', 'UIDocumentPickerDelegate', 'UIViewControllerInteractiveTransitioning', 'GKTurnBasedEventListener', 'SCNSceneRenderer', 'MTLTexture', 'GLKViewDelegate', 'EAAccessoryDelegate', 'WKScriptMessageHandler', 'PHPhotoLibraryChangeObserver', 'NSKeyedUnarchiverDelegate', 'AVPlayerItemMetadataOutputPushDelegate', 'NSMachPortDelegate', 'SCNShadable', 'UIPopoverBackgroundViewMethods', 'UIDocumentMenuDelegate', 'UIBarPositioningDelegate', 'ABPersonViewControllerDelegate', 'NSNetServiceBrowserDelegate', 'EKEventViewDelegate', 'UIScrollViewDelegate', 'NSURLConnectionDownloadDelegate', 'UIGestureRecognizerDelegate', 'UINavigationBarDelegate', 'AVAudioMixing', 'NSFetchedResultsSectionInfo', 'UIDocumentInteractionControllerDelegate', 'MTLParallelRenderCommandEncoder', 'QLPreviewControllerDelegate', 'UIAccessibilityReadingContent', 'ABUnknownPersonViewControllerDelegate', 'GLKViewControllerDelegate', 'UICollectionViewDelegateFlowLayout', 'UIPopoverPresentationControllerDelegate', 'UIDynamicAnimatorDelegate', 'NSTextAttachmentContainer', 'MKAnnotation', 'UIAccessibilityIdentification', 'UICoordinateSpace', 'ABNewPersonViewControllerDelegate', 'MTLDevice', 'CAMediaTiming', 'AVCaptureFileOutputRecordingDelegate', 'HMHomeManagerDelegate', 'UITextViewDelegate', 'UITabBarDelegate', 'GKLeaderboardViewControllerDelegate', 'UISearchControllerDelegate', 'EAWiFiUnconfiguredAccessoryBrowserDelegate', 'UITextInputTraits', 'MTLRenderPipelineState', 'GKVoiceChatClient', 'UIKeyInput', 'UICollectionViewDataSource', 'SCNTechniqueSupport', 'NSLocking', 'AVCaptureFileOutputDelegate', 'GKChallengeEventHandlerDelegate', 'UIObjectRestoration', 'CIFilterConstructor', 'AVPlayerItemOutputPullDelegate', 'EAGLDrawable', 'AVVideoCompositionValidationHandling', 'UIViewControllerAnimatedTransitioning', 'NSURLSessionDownloadDelegate', 'UIAccelerometerDelegate', 'UIPageViewControllerDelegate', 'MTLCommandQueue', 'UIDataSourceModelAssociation', 'AVAudioRecorderDelegate', 'GKSessionDelegate', 'NSKeyedArchiverDelegate', 'CAMetalDrawable', 'UIDynamicItem', 'CLLocationManagerDelegate', 'NSMetadataQueryDelegate', 'NSNetServiceDelegate', 'GKMatchmakerViewControllerDelegate', 'NSURLSessionDataDelegate'}
COCOA_PRIMITIVES = {'ROTAHeader', '__CFBundle', 'MortSubtable', 'AudioFilePacketTableInfo', 'CGPDFOperatorTable', 'KerxStateEntry', 'ExtendedTempoEvent', 'CTParagraphStyleSetting', 'OpaqueMIDIPort', '_GLKMatrix3', '_GLKMatrix2', '_GLKMatrix4', 'ExtendedControlEvent', 'CAFAudioDescription', 'OpaqueCMBlockBuffer', 'CGTextDrawingMode', 'EKErrorCode', 'gss_buffer_desc_struct', 'AudioUnitParameterInfo', '__SCPreferences', '__CTFrame', '__CTLine', 'AudioFile_SMPTE_Time', 'gss_krb5_lucid_context_v1', 'OpaqueJSValue', 'TrakTableEntry', 'AudioFramePacketTranslation', 'CGImageSource', 'OpaqueJSPropertyNameAccumulator', 'JustPCGlyphRepeatAddAction', '__CFBinaryHeap', 'OpaqueMIDIThruConnection', 'opaqueCMBufferQueue', 'OpaqueMusicSequence', 'MortRearrangementSubtable', 'MixerDistanceParams', 'MorxSubtable', 'MIDIObjectPropertyChangeNotification', 'SFNTLookupSegment', 'CGImageMetadataErrors', 'CGPath', 'OpaqueMIDIEndpoint', 'AudioComponentPlugInInterface', 'gss_ctx_id_t_desc_struct', 'sfntFontFeatureSetting', 'OpaqueJSContextGroup', '__SCNetworkConnection', 'AudioUnitParameterValueTranslation', 'CGImageMetadataType', 'CGPattern', 'AudioFileTypeAndFormatID', 'CGContext', 'AUNodeInteraction', 'SFNTLookupTable', 'JustPCDecompositionAction', 'KerxControlPointHeader', 'AudioStreamPacketDescription', 'KernSubtableHeader', '__SecCertificate', 'AUMIDIOutputCallbackStruct', 'MIDIMetaEvent', 'AudioQueueChannelAssignment', 'AnchorPoint', 'JustTable', '__CFNetService', 'CF_BRIDGED_TYPE', 'gss_krb5_lucid_key', 'CGPDFDictionary', 'KerxSubtableHeader', 'CAF_UUID_ChunkHeader', 'gss_krb5_cfx_keydata', 'OpaqueJSClass', 'CGGradient', 'OpaqueMIDISetup', 'JustPostcompTable', '__CTParagraphStyle', 'AudioUnitParameterHistoryInfo', 'OpaqueJSContext', 'CGShading', 'MIDIThruConnectionParams', 'BslnFormat0Part', 'SFNTLookupSingle', '__CFHost', '__SecRandom', '__CTFontDescriptor', '_NSRange', 'sfntDirectory', 'AudioQueueLevelMeterState', 'CAFPositionPeak', 'PropLookupSegment', '__CVOpenGLESTextureCache', 'sfntInstance', '_GLKQuaternion', 'AnkrTable', '__SCNetworkProtocol', 'CAFFileHeader', 'KerxOrderedListHeader', 'CGBlendMode', 'STXEntryOne', 'CAFRegion', 'SFNTLookupTrimmedArrayHeader', 'SCNMatrix4', 'KerxControlPointEntry', 'OpaqueMusicTrack', '_GLKVector4', 'gss_OID_set_desc_struct', 'OpaqueMusicPlayer', '_CFHTTPAuthentication', 'CGAffineTransform', 'CAFMarkerChunk', 'AUHostIdentifier', 'ROTAGlyphEntry', 'BslnTable', 'gss_krb5_lucid_context_version', '_GLKMatrixStack', 'CGImage', 'KernStateEntry', 'SFNTLookupSingleHeader', 'MortLigatureSubtable', 'CAFUMIDChunk', 'SMPTETime', 'CAFDataChunk', 'CGPDFStream', 'AudioFileRegionList', 'STEntryTwo', 'SFNTLookupBinarySearchHeader', 'OpbdTable', '__CTGlyphInfo', 'BslnFormat2Part', 'KerxIndexArrayHeader', 'TrakTable', 'KerxKerningPair', '__CFBitVector', 'KernVersion0SubtableHeader', 'OpaqueAudioComponentInstance', 'AudioChannelLayout', '__CFUUID', 'MIDISysexSendRequest', '__CFNumberFormatter', 'CGImageSourceStatus', 'AudioFileMarkerList', 'AUSamplerBankPresetData', 'CGDataProvider', 'AudioFormatInfo', '__SecIdentity', 'sfntCMapExtendedSubHeader', 'MIDIChannelMessage', 'KernOffsetTable', 'CGColorSpaceModel', 'MFMailComposeErrorCode', 'CGFunction', '__SecTrust', 'AVAudio3DAngularOrientation', 'CGFontPostScriptFormat', 'KernStateHeader', 'AudioUnitCocoaViewInfo', 'CGDataConsumer', 'OpaqueMIDIDevice', 'KernVersion0Header', 'AnchorPointTable', 'CGImageDestination', 'CAFInstrumentChunk', 'AudioUnitMeterClipping', 'MorxChain', '__CTFontCollection', 'STEntryOne', 'STXEntryTwo', 'ExtendedNoteOnEvent', 'CGColorRenderingIntent', 'KerxSimpleArrayHeader', 'MorxTable', '_GLKVector3', '_GLKVector2', 'MortTable', 'CGPDFBox', 'AudioUnitParameterValueFromString', '__CFSocket', 'ALCdevice_struct', 'MIDINoteMessage', 'sfntFeatureHeader', 'CGRect', '__SCNetworkInterface', '__CFTree', 'MusicEventUserData', 'TrakTableData', 'GCQuaternion', 'MortContextualSubtable', '__CTRun', 'AudioUnitFrequencyResponseBin', 'MortChain', 'MorxInsertionSubtable', 'CGImageMetadata', 'gss_auth_identity', 'AudioUnitMIDIControlMapping', 'CAFChunkHeader', 'CGImagePropertyOrientation', 'CGPDFScanner', 'OpaqueMusicEventIterator', 'sfntDescriptorHeader', 'AudioUnitNodeConnection', 'OpaqueMIDIDeviceList', 'ExtendedAudioFormatInfo', 'BslnFormat1Part', 'sfntFontDescriptor', 'KernSimpleArrayHeader', '__CFRunLoopObserver', 'CGPatternTiling', 'MIDINotification', 'MorxLigatureSubtable', 'MessageComposeResult', 'MIDIThruConnectionEndpoint', 'MusicDeviceStdNoteParams', 'opaqueCMSimpleQueue', 'ALCcontext_struct', 'OpaqueAudioQueue', 'PropLookupSingle', 'CGInterpolationQuality', 'CGColor', 'AudioOutputUnitStartAtTimeParams', 'gss_name_t_desc_struct', 'CGFunctionCallbacks', 'CAFPacketTableHeader', 'AudioChannelDescription', 'sfntFeatureName', 'MorxContextualSubtable', 'CVSMPTETime', 'AudioValueRange', 'CGTextEncoding', 'AudioStreamBasicDescription', 'AUNodeRenderCallback', 'AudioPanningInfo', 'KerxOrderedListEntry', '__CFAllocator', 'OpaqueJSPropertyNameArray', '__SCDynamicStore', 'OpaqueMIDIEntity', '__CTRubyAnnotation', 'SCNVector4', 'CFHostClientContext', 'CFNetServiceClientContext', 'AudioUnitPresetMAS_SettingData', 'opaqueCMBufferQueueTriggerToken', 'AudioUnitProperty', 'CAFRegionChunk', 'CGPDFString', '__GLsync', '__CFStringTokenizer', 'JustWidthDeltaEntry', 'sfntVariationAxis', '__CFNetDiagnostic', 'CAFOverviewSample', 'sfntCMapEncoding', 'CGVector', '__SCNetworkService', 'opaqueCMSampleBuffer', 'AUHostVersionIdentifier', 'AudioBalanceFade', 'sfntFontRunFeature', 'KerxCoordinateAction', 'sfntCMapSubHeader', 'CVPlanarPixelBufferInfo', 'AUNumVersion', 'AUSamplerInstrumentData', 'AUPreset', '__CTRunDelegate', 'OpaqueAudioQueueProcessingTap', 'KerxTableHeader', '_NSZone', 'OpaqueExtAudioFile', '__CFRunLoopSource', '__CVMetalTextureCache', 'KerxAnchorPointAction', 'OpaqueJSString', 'AudioQueueParameterEvent', '__CFHTTPMessage', 'OpaqueCMClock', 'ScheduledAudioFileRegion', 'STEntryZero', 'AVAudio3DPoint', 'gss_channel_bindings_struct', 'sfntVariationHeader', 'AUChannelInfo', 'UIOffset', 'GLKEffectPropertyPrv', 'KerxStateHeader', 'CGLineJoin', 'CGPDFDocument', '__CFBag', 'KernOrderedListHeader', '__SCNetworkSet', '__SecKey', 'MIDIObjectAddRemoveNotification', 'AudioUnitParameter', 'JustPCActionSubrecord', 'AudioComponentDescription', 'AudioUnitParameterValueName', 'AudioUnitParameterEvent', 'KerxControlPointAction', 'AudioTimeStamp', 'KernKerningPair', 'gss_buffer_set_desc_struct', 'MortFeatureEntry', 'FontVariation', 'CAFStringID', 'LcarCaretClassEntry', 'AudioUnitParameterStringFromValue', 'ACErrorCode', 'ALMXGlyphEntry', 'LtagTable', '__CTTypesetter', 'AuthorizationOpaqueRef', 'UIEdgeInsets', 'CGPathElement', 'CAFMarker', 'KernTableHeader', 'NoteParamsControlValue', 'SSLContext', 'gss_cred_id_t_desc_struct', 'AudioUnitParameterNameInfo', 'CGDataConsumerCallbacks', 'ALMXHeader', 'CGLineCap', 'MIDIControlTransform', 'CGPDFArray', '__SecPolicy', 'AudioConverterPrimeInfo', '__CTTextTab', '__CFNetServiceMonitor', 'AUInputSamplesInOutputCallbackStruct', '__CTFramesetter', 'CGPDFDataFormat', 'STHeader', 'CVPlanarPixelBufferInfo_YCbCrPlanar', 'MIDIValueMap', 'JustDirectionTable', '__SCBondStatus', 'SFNTLookupSegmentHeader', 'OpaqueCMMemoryPool', 'CGPathDrawingMode', 'CGFont', '__SCNetworkReachability', 'AudioClassDescription', 'CGPoint', 'AVAudio3DVectorOrientation', 'CAFStrings', '__CFNetServiceBrowser', 'opaqueMTAudioProcessingTap', 'sfntNameRecord', 'CGPDFPage', 'CGLayer', 'ComponentInstanceRecord', 'CAFInfoStrings', 'HostCallbackInfo', 'MusicDeviceNoteParams', 'OpaqueVTCompressionSession', 'KernIndexArrayHeader', 'CVPlanarPixelBufferInfo_YCbCrBiPlanar', 'MusicTrackLoopInfo', 'opaqueCMFormatDescription', 'STClassTable', 'sfntDirectoryEntry', 'OpaqueCMTimebase', 'CGDataProviderDirectCallbacks', 'MIDIPacketList', 'CAFOverviewChunk', 'MIDIPacket', 'ScheduledAudioSlice', 'CGDataProviderSequentialCallbacks', 'AudioBuffer', 'MorxRearrangementSubtable', 'CGPatternCallbacks', 'AUDistanceAttenuationData', 'MIDIIOErrorNotification', 'CGPDFContentStream', 'IUnknownVTbl', 'MIDITransform', 'MortInsertionSubtable', 'CABarBeatTime', 'AudioBufferList', '__CVBuffer', 'AURenderCallbackStruct', 'STXEntryZero', 'JustPCDuctilityAction', 'OpaqueAudioQueueTimeline', 'VTDecompressionOutputCallbackRecord', 'OpaqueMIDIClient', '__CFPlugInInstance', 'AudioQueueBuffer', '__CFFileDescriptor', 'AudioUnitConnection', '_GKTurnBasedExchangeStatus', 'LcarCaretTable', 'CVPlanarComponentInfo', 'JustWidthDeltaGroup', 'OpaqueAudioComponent', 'ParameterEvent', '__CVPixelBufferPool', '__CTFont', 'CGColorSpace', 'CGSize', 'AUDependentParameter', 'MIDIDriverInterface', 'gss_krb5_rfc1964_keydata', '__CFDateFormatter', 'LtagStringRange', 'OpaqueVTDecompressionSession', 'gss_iov_buffer_desc_struct', 'AUPresetEvent', 'PropTable', 'KernOrderedListEntry', 'CF_BRIDGED_MUTABLE_TYPE', 'gss_OID_desc_struct', 'AudioUnitPresetMAS_Settings', 'AudioFileMarker', 'JustPCConditionalAddAction', 'BslnFormat3Part', '__CFNotificationCenter', 'MortSwashSubtable', 'AUParameterMIDIMapping', 'SCNVector3', 'OpaqueAudioConverter', 'MIDIRawData', 'sfntNameHeader', '__CFRunLoop', 'MFMailComposeResult', 'CATransform3D', 'OpbdSideValues', 'CAF_SMPTE_Time', '__SecAccessControl', 'JustPCAction', 'OpaqueVTFrameSilo', 'OpaqueVTMultiPassStorage', 'CGPathElementType', 'AudioFormatListItem', 'AudioUnitExternalBuffer', 'AudioFileRegion', 'AudioValueTranslation', 'CGImageMetadataTag', 'CAFPeakChunk', 'AudioBytePacketTranslation', 'sfntCMapHeader', '__CFURLEnumerator', 'STXHeader', 'CGPDFObjectType', 'SFNTLookupArrayHeader'}

if __name__ == '__main__':  # pragma: no cover
    import os
    import re

    FRAMEWORKS_PATH = '/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS8.1.sdk/System/Library/Frameworks/'
    frameworks = os.listdir(FRAMEWORKS_PATH)

    all_interfaces = set()
    all_protocols  = set()
    all_primitives = set()
    for framework in frameworks:
        frameworkHeadersDir = FRAMEWORKS_PATH + framework + '/Headers/'
        if not os.path.exists(frameworkHeadersDir):
            continue

        headerFilenames = os.listdir(frameworkHeadersDir)

        for f in headerFilenames:
            if not f.endswith('.h'):
                continue

            headerFilePath = frameworkHeadersDir + f
            with open(headerFilePath) as f:
                content = f.read()
            res = re.findall(r'(?<=@interface )\w+', content)
            for r in res:
                all_interfaces.add(r)

            res = re.findall(r'(?<=@protocol )\w+', content)
            for r in res:
                all_protocols.add(r)

            res = re.findall(r'(?<=typedef enum )\w+', content)
            for r in res:
                all_primitives.add(r)

            res = re.findall(r'(?<=typedef struct )\w+', content)
            for r in res:
                all_primitives.add(r)

            res = re.findall(r'(?<=typedef const struct )\w+', content)
            for r in res:
                all_primitives.add(r)


    print("ALL interfaces: \n")
    print(all_interfaces)

    print("\nALL protocols: \n")
    print(all_protocols)

    print("\nALL primitives: \n")
    print(all_primitives)
