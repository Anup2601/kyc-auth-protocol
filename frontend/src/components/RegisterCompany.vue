<template>
    <div>
        <!-- Company Registration Form -->
    <div v-if="currentStep === 'company-form'" class="step-container company-form">
      <transition name="slide-fade">
        <div>
          <h1>Create company account</h1>
          <p class="subtitle">Company information</p>
          
          <!-- Profile Picture Upload -->
          <div class="profile-pic-upload">
            <div v-if="!profilePicPreview" class="profile-placeholder" @click="triggerProfilePicUpload">
              <div class="profile-icon">🏢</div>
              <div class="upload-text">Upload logo</div>
            </div>
            <div v-else class="profile-preview" @click="triggerProfilePicUpload">
              <img :src="profilePicPreview" alt="Company Logo" class="preview-image">
              <div class="overlay">Change</div>
            </div>
            <input 
              type="file" 
              ref="profilePicInput" 
              @change="handleProfilePicUpload" 
              accept="image/*" 
              class="file-input"
            >
          </div>
          
          <div class="form-control" :class="{ 'focused': isOrgNameFocused || orgName }">
            <input 
              type="text" 
              id="orgName" 
              v-model="orgName" 
              @focus="isOrgNameFocused = true" 
              @blur="isOrgNameFocused = false"
              placeholder=" "
            >
            <label for="orgName">Organization name</label>
          </div>
          
          <div class="form-grid">
            <div class="form-control" :class="{ 'focused': isGovIssueNoFocused || govIssueNo }">
              <input 
                type="text" 
                id="govIssueNo" 
                v-model="govIssueNo" 
                @focus="isGovIssueNoFocused = true" 
                @blur="isGovIssueNoFocused = false"
                placeholder=" "
              >
              <label for="govIssueNo">Registration number</label>
            </div>
            
            <div class="form-control" :class="{ 'focused': isPhoneFocused || phone }">
              <input 
                type="tel" 
                id="phone" 
                v-model="phone" 
                @focus="isPhoneFocused = true" 
                @blur="isPhoneFocused = false"
                placeholder=" "
              >
              <label for="phone">Phone number</label>
            </div>
          </div>
          
          <div class="form-control" :class="{ 'focused': isEmailFocused || email }">
            <input 
              type="email" 
              id="email" 
              v-model="email" 
              @focus="isEmailFocused = true" 
              @blur="isEmailFocused = false"
              placeholder=" "
            >
            <label for="email">Business email</label>
          </div>
          
          <div class="form-control" :class="{ 'focused': isAddressFocused || address }">
            <input 
              type="text" 
              id="address" 
              v-model="address" 
              @focus="isAddressFocused = true" 
              @blur="isAddressFocused = false"
              placeholder=" "
            >
            <label for="address">Business address</label>
          </div>
          
          <div class="form-grid">
            <div class="form-control" :class="{ 'focused': isCityFocused || city }">
              <input 
                type="text" 
                id="city" 
                v-model="city" 
                @focus="isCityFocused = true" 
                @blur="isCityFocused = false"
                placeholder=" "
              >
              <label for="city">City</label>
            </div>
            
            <div class="form-control" :class="{ 'focused': isZipCodeFocused || zipCode }">
              <input 
                type="text" 
                id="zipCode" 
                v-model="zipCode" 
                @focus="isZipCodeFocused = true" 
                @blur="isZipCodeFocused = false"
                placeholder=" "
              >
              <label for="zipCode">ZIP / Postal code</label>
            </div>
          </div>
          
          <div class="form-control" :class="{ 'focused': isNationalityFocused || nationality }">
            <select 
              id="nationality" 
              v-model="nationality" 
              @focus="isNationalityFocused = true" 
              @blur="isNationalityFocused = false"
              class="select-input"
            >
              <option value="" disabled selected>Select country</option>
              <option value="us">United States</option>
              <option value="uk">United Kingdom</option>
              <option value="ca">Canada</option>
              <option value="au">Australia</option>
              <option value="in">India</option>
              <option value="sg">Singapore</option>
              <!-- Add more countries as needed -->
            </select>
            <label for="nationality">Country / Region</label>
          </div>
          
          <div class="form-grid">
            <div class="form-control" :class="{ 'focused': isPasswordFocused || password }">
              <input 
                :type="showPassword ? 'text' : 'password'" 
                id="password" 
                v-model="password" 
                @focus="isPasswordFocused = true" 
                @blur="isPasswordFocused = false"
                placeholder=" "
              >
              <label for="password">Password</label>
              <button type="button" class="toggle-password" @click="showPassword = !showPassword">
                {{ showPassword ? '🙈' : '👁️' }}
              </button>
            </div>
            
            <div class="form-control" :class="{ 'focused': isConfirmPasswordFocused || confirmPassword }">
              <input 
                :type="showConfirmPassword ? 'text' : 'password'" 
                id="confirmPassword" 
                v-model="confirmPassword" 
                @focus="isConfirmPasswordFocused = true" 
                @blur="isConfirmPasswordFocused = false"
                placeholder=" "
              >
              <label for="confirmPassword">Confirm</label>
              <button type="button" class="toggle-password" @click="showConfirmPassword = !showConfirmPassword">
                {{ showConfirmPassword ? '🙈' : '👁️' }}
              </button>
            </div>
          </div>
          
          <div class="bottom-container">
            <button class="back-btn" @click="goToSelectionStep">
              <span class="back-icon">‹</span> Back
            </button>
            <button class="next-btn" @click="goToCompanyDocumentStep" :class="{ 'hovered': isNextHovered }" @mouseover="isNextHovered = true" @mouseleave="isNextHovered = false">Next</button>
          </div>
        </div>
      </transition>
    </div>
    
    <!-- Company Document Verification -->
     
    <div v-if="currentStep === 'company-document-verification'" class="step-container document-verification">
      <transition name="slide-fade">
        <div>
          <h1>Business Verification</h1>
          <p class="subtitle">Please upload required verification documents</p>
          
          <div class="verification-tabs">
            <div class="tab" :class="{ 'active': activeTab === 'registration' }" @click="activeTab = 'registration'">
              Business Registration
            </div>
            <div class="tab" :class="{ 'active': activeTab === 'kyc' }" @click="activeTab = 'kyc'">
              KYC Document
            </div>
          </div>
          
          <!-- Registration Document Tab -->
          <div v-if="activeTab === 'registration'" class="tab-content">
            <p class="document-instruction">Upload your business registration certificate</p>
            
            <div class="verification-options">
              <div class="verification-option" @click="showRegistrationFileUpload = true">
                <div class="option-icon">📁</div>
                <div class="option-title">Upload Document</div>
                <div class="option-description">Upload an image of your registration certificate</div>
              </div>
              
              <div class="verification-option" @click="openRegistrationCamera">
                <div class="option-icon">📷</div>
                <div class="option-title">Scan with Camera</div>
                <div class="option-description">Use your camera to scan your document</div>
              </div>
            </div>
            
            <!-- File Upload Area (hidden by default) -->
            <div v-if="showRegistrationFileUpload" class="file-upload-area">
              <input type="file" id="registrationUpload" ref="registrationFileInput" @change="handleRegistrationFileUpload" accept="image/*" class="file-input">
              <label for="registrationUpload" class="file-input-label">
                <div v-if="!registrationFile">
                  <div class="upload-icon">📄</div>
                  <div>Drag and drop your file here or</div>
                  <button class="browse-btn">Browse files</button>
                </div>
                <div v-else class="uploaded-file">
                  <div class="file-preview">
                    <img v-if="registrationFilePreview" :src="registrationFilePreview" alt="Document Preview" class="id-preview">
                    <div v-else class="file-name">{{ registrationFile.name }}</div>
                  </div>
                  <button class="remove-file" @click.prevent="removeRegistrationFile">Remove</button>
                </div>
              </label>
            </div>
            
            <!-- Camera Capture (hidden by default) -->
            <div v-if="showRegistrationCamera" class="camera-capture">
              <video ref="registrationVideo" class="camera-video" autoplay></video>
              <div class="camera-controls">
                <button class="camera-btn" @click="captureRegistrationPhoto">Capture</button>
                <button class="camera-btn cancel" @click="closeRegistrationCamera">Cancel</button>
              </div>
            </div>
            
            <!-- Captured Photo (hidden by default) -->
            <div v-if="capturedRegistrationImage" class="captured-image-container">
              <img :src="capturedRegistrationImage" alt="Captured Document" class="captured-image">
              <div class="camera-controls">
                <button class="camera-btn" @click="acceptRegistrationImage">Accept</button>
                <button class="camera-btn cancel" @click="retakeRegistrationPhoto">Retake</button>
              </div>
            </div>
          </div>
          
          <!-- KYC Document Tab -->
          <div v-if="activeTab === 'kyc'" class="tab-content">
            <p class="document-instruction">Upload your KYC verification document</p>
            
            <div class="verification-options">
              <div class="verification-option" @click="showKycFileUpload = true">
                <div class="option-icon">📁</div>
                <div class="option-title">Upload Document</div>
                <div class="option-description">Upload an image of your KYC document</div>
              </div>
              
              <div class="verification-option" @click="openKycCamera">
                <div class="option-icon">📷</div>
                <div class="option-title">Scan with Camera</div>
                <div class="option-description">Use your camera to scan your document</div>
              </div>
            </div>
            
            <!-- File Upload Area (hidden by default) -->
            <div v-if="showKycFileUpload" class="file-upload-area">
              <input type="file" id="kycUpload" ref="kycFileInput" @change="handleKycFileUpload" accept="image/*" class="file-input">
              <label for="kycUpload" class="file-input-label">
                <div v-if="!kycFile">
                  <div class="upload-icon">📄</div>
                  <div>Drag and drop your file here or</div>
                  <button class="browse-btn">Browse files</button>
                </div>
                <div v-else class="uploaded-file">
                  <div class="file-preview">
                    <img v-if="kycFilePreview" :src="kycFilePreview" alt="KYC Preview" class="id-preview">
                    <div v-else class="file-name">{{ kycFile.name }}</div>
                  </div>
                  <button class="remove-file" @click.prevent="removeKycFile">Remove</button>
                </div>
              </label>
            </div>
            
            <!-- Camera Capture (hidden by default) -->
            <div v-if="showKycCamera" class="camera-capture">
              <video ref="kycVideo" class="camera-video" autoplay></video>
              <div class="camera-controls">
                <button class="camera-btn" @click="captureKycPhoto">Capture</button>
                <button class="camera-btn cancel" @click="closeKycCamera">Cancel</button>
              </div>
            </div>
            
            <!-- Captured Photo (hidden by default) -->
            <div v-if="capturedKycImage" class="captured-image-container">
              <img :src="capturedKycImage" alt="Captured KYC" class="captured-image">
              <div class="camera-controls">
                <button class="camera-btn" @click="acceptKycImage">Accept</button>
                <button class="camera-btn cancel" @click="retakeKycPhoto">Retake</button>
              </div>
            </div>
          </div>
          
          <div class="verification-status">
            <div class="status-icon">⚠️</div>
            <div class="status-text">
              <strong>KYC Verification Status: </strong>
              <span class="pending">Pending</span>
            </div>
          </div>
          
          <div class="bottom-container">
            <button class="back-btn" @click="goToCompanyFormStep">
              <span class="back-icon">‹</span> Back
            </button>
            <button class="next-btn" @click="completeCompanyRegistration" :disabled="!isCompanyDocumentUploaded" :class="{ 'hovered': isNextHovered }" @mouseover="isNextHovered = true" @mouseleave="isNextHovered = false">Complete Registration</button>
          </div>
        </div>
      </transition>
    </div>
    </div>
  </template>
  
  <script>
  // Add this to the existing script section
  export default {
    name: 'RegisterCompany',
    data() {
      return {
        currentStep: 'company-document-verification',
        
        // Company form fields
        orgName: '',
        govIssueNo: '',
        phone: '',
        address: '',
        city: '',
        zipCode: '',
        nationality: '',
        
        // Company form focus states
        isOrgNameFocused: false,
        isGovIssueNoFocused: false,
        isPhoneFocused: false,
        isAddressFocused: false,
        isCityFocused: false,
        isZipCodeFocused: false,
        isNationalityFocused: false,
        
        // Company profile picture
        profilePicFile: null,
        profilePicPreview: null,
        
        // Company document verification
        activeTab: 'registration',
        
        // Registration document
        showRegistrationFileUpload: false,
        showRegistrationCamera: false,
        registrationFile: null,
        registrationFilePreview: null,
        capturedRegistrationImage: null,
        registrationStream: null,
        
        // KYC document
        showKycFileUpload: false,
        showKycCamera: false,
        kycFile: null,
        kycFilePreview: null,
        capturedKycImage: null,
        kycStream: null,
        
        isCompanyDocumentUploaded: false
      }
    },
    methods: {
      // Modify the existing methods
      goToNextStep() {
        if (!this.accountType) return;
        
        if (this.accountType === 'user') {
          this.currentStep = 'user-form';
        } else if (this.accountType === 'company') {
          this.currentStep = 'company-form';
        }
      },
      
      // Add new methods for company registration
      goToCompanyFormStep() {
        this.currentStep = 'company-form';
      },
      
      goToCompanyDocumentStep() {
        if (!this.validateCompanyForm()) return;
        this.currentStep = 'company-document-verification';
      },
      
      validateCompanyForm() {
        // Basic validation for company form
        if (!this.orgName) {
          alert('Please enter your organization name');
          return false;
        }
        if (!this.govIssueNo) {
          alert('Please enter your government issue number');
          return false;
        }
        if (!this.phone) {
          alert('Please enter your phone number');
          return false;
        }
        if (!this.email || !this.email.includes('@')) {
          alert('Please enter a valid email address');
          return false;
        }
        if (!this.address) {
          alert('Please enter your business address');
          return false;
        }
        if (!this.city) {
          alert('Please enter your city');
          return false;
        }
        if (!this.zipCode) {
          alert('Please enter your ZIP/Postal code');
          return false;
        }
        if (!this.nationality) {
          alert('Please select your country/region');
          return false;
        }
        if (!this.password || this.password.length < 8) {
          alert('Password must be at least 8 characters');
          return false;
        }
        if (this.password !== this.confirmPassword) {
          alert('Passwords do not match');
          return false;
        }
        return true;
      },
      
      // Profile Picture Methods
      triggerProfilePicUpload() {
        this.$refs.profilePicInput.click();
      },
      
      handleProfilePicUpload(event) {
        const file = event.target.files[0];
        if (!file) return;
        
        this.profilePicFile = file;
        
        // Create file preview
        const reader = new FileReader();
        reader.onload = e => {
          this.profilePicPreview = e.target.result;
        };
        reader.readAsDataURL(file);
      },
      
      // Registration Document Methods
      handleRegistrationFileUpload(event) {
        const file = event.target.files[0];
        if (!file) return;
        
        this.registrationFile = file;
        this.isCompanyDocumentUploaded = true;
        
        // Create file preview
        const reader = new FileReader();
        reader.onload = e => {
          this.registrationFilePreview = e.target.result;
        };
        reader.readAsDataURL(file);
      },
      
      removeRegistrationFile() {
        this.registrationFile = null;
        this.registrationFilePreview = null;
        this.isCompanyDocumentUploaded = this.kycFile !== null;
        if (this.$refs.registrationFileInput) {
          this.$refs.registrationFileInput.value = '';
        }
      },
      
      openRegistrationCamera() {
        this.showRegistrationFileUpload = false;
        this.showRegistrationCamera = true;
        
        // Access the camera
        navigator.mediaDevices.getUserMedia({ video: true })
          .then(stream => {
            this.registrationStream = stream;
            this.$refs.registrationVideo.srcObject = stream;
          })
          .catch(err => {
            console.error('Error accessing camera:', err);
            alert('Could not access camera. Please ensure you have granted camera permissions.');
            this.showRegistrationCamera = false;
          });
      },
      
      closeRegistrationCamera() {
        if (this.registrationStream) {
          this.registrationStream.getTracks().forEach(track => track.stop());
          this.registrationStream = null;
        }
        this.showRegistrationCamera = false;
      },
      
      captureRegistrationPhoto() {
        const video = this.$refs.registrationVideo;
        const canvas = document.createElement('canvas');
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
        const ctx = canvas.getContext('2d');
        ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
        
        this.capturedRegistrationImage = canvas.toDataURL('image/png');
        this.closeRegistrationCamera();
      },
      
      retakeRegistrationPhoto() {
        this.capturedRegistrationImage = null;
        this.openRegistrationCamera();
      },
      
      acceptRegistrationImage() {
        this.isCompanyDocumentUploaded = true;
        this.capturedRegistrationImage = this.capturedRegistrationImage; // Keep the captured image
      },
      
      // KYC Document Methods
      handleKycFileUpload(event) {
        const file = event.target.files[0];
        if (!file) return;
        
        this.kycFile = file;
        this.isCompanyDocumentUploaded = true;
        
        // Create file preview
        const reader = new FileReader();
        reader.onload = e => {
          this.kycFilePreview = e.target.result;
        };
        reader.readAsDataURL(file);
      },
      
      removeKycFile() {
        this.kycFile = null;
        this.kycFilePreview = null;
        this.isCompanyDocumentUploaded = this.registrationFile !== null;
        if (this.$refs.kycFileInput) {
          this.$refs.kycFileInput.value = '';
        }
      },
      
      openKycCamera() {
        this.showKycFileUpload = false;
        this.showKycCamera = true;
        
        // Access the camera
        navigator.mediaDevices.getUserMedia({ video: true })
          .then(stream => {
            this.kycStream = stream;
            this.$refs.kycVideo.srcObject = stream;
          })
          .catch(err => {
            console.error('Error accessing camera:', err);
            alert('Could not access camera. Please ensure you have granted camera permissions.');
            this.showKycCamera = false;
          });
      },
      
      closeKycCamera() {
        if (this.kycStream) {
          this.kycStream.getTracks().forEach(track => track.stop());
          this.kycStream = null;
        }
        this.showKycCamera = false;
      },
      
      captureKycPhoto() {
        const video = this.$refs.kycVideo;
        const canvas = document.createElement('canvas');
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
        const ctx = canvas.getContext('2d');
        ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
        
        this.capturedKycImage = canvas.toDataURL('image/png');
        this.closeKycCamera();
      },
      
      retakeKycPhoto() {
        this.capturedKycImage = null;
        this.openKycCamera();
      },
      
      acceptKycImage() {
        this.isCompanyDocumentUploaded = true;
        this.capturedKycImage = this.capturedKycImage; // Keep the captured image
      },
      
      completeCompanyRegistration() {
        if (!this.isCompanyDocumentUploaded) {
          alert('Please upload at least one verification document');
          return;
        }
        
        // In a real app, you would submit the form to your backend
        console.log('Company Registration data:', {
          accountType: this.accountType,
          orgName: this.orgName,
          govIssueNo: this.govIssueNo,
          phone: this.phone,
          email: this.email,
          address: this.address,
          city: this.city,
          zipCode: this.zipCode,
          nationality: this.nationality,
          profilePicUploaded: !!this.profilePicFile,
          registrationDocUploaded: !!this.registrationFile || !!this.capturedRegistrationImage,
          kycDocUploaded: !!this.kycFile || !!this.capturedKycImage,
          kycStatus: 'pending'
        });
        
        // Show success message
        this.currentStep = 'success';
      },
      
      beforeUnmount() {
        // Clean up camera resources when component is destroyed
        if (this.stream) {
          this.stream.getTracks().forEach(track => track.stop());
        }
        if (this.registrationStream) {
          this.registrationStream.getTracks().forEach(track => track.stop());
        }
        if (this.kycStream) {
          this.kycStream.getTracks().forEach(track => track.stop());
        }
      }
    }
  }
  </script>
  
  <style scoped>
  /* Add these styles to your existing CSS */
  
  /* Profile Picture Upload */
  .profile-pic-upload {
    margin: 0 auto 24px;
    width: 120px;
    height: 120px;
    position: relative;
    cursor: pointer;
  }
  
  .profile-placeholder {
    width: 100%;
    height: 100%;
    border-radius: 50%;
    background-color: #f1f3f4;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    border: 2px dashed #dadce0;
    transition: all 0.3s;
  }
  
  .profile-placeholder:hover {
    background-color: #e8f0fe;
    border-color: #1a73e8;
  }
  
  .profile-icon {
    font-size: 40px;
    margin-bottom: 5px;
    color: #5f6368;
  }
  
  .upload-text {
    font-size: 12px;
    color: #1a73e8;
  }
  
  .profile-preview {
    width: 100%;
    height: 100%;
    border-radius: 50%;
    overflow: hidden;
    position: relative;
  }
  
  .preview-image {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
  
  .overlay {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: rgba(0, 0, 0, 0.5);
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    opacity: 0;
    transition: opacity 0.3s;
  }
  
  .profile-preview:hover .overlay {
    opacity: 1;
  }
  
  /* Tabs */
  .verification-tabs {
    display: flex;
    border-bottom: 1px solid #dadce0;
    margin-bottom: 25px;
  }
  
  .tab {
    padding: 12px 24px;
    cursor: pointer;
    transition: all 0.3s;
    font-size: 14px;
    color: #5f6368;
    position: relative;
  }
  
  .tab:hover {
    color: #1a73e8;
  }
  
  .tab.active {
    color: #1a73e8;
    font-weight: 500;
  }
  
  .tab.active::after {
    content: '';
    position: absolute;
    bottom: -1px;
    left: 0;
    width: 100%;
    height: 3px;
    background-color: #1a73e8;
  }
  
  .tab-content {
    padding: 20px 0;
    animation: fadeIn 0.5s;
  }
  
  .document-instruction {
    font-size: 14px;
    color: #5f6368;
    margin-bottom: 20px;
  }
  
  /* Form Control Updates */
  .form-control.select-input {
    position: relative;
  }
  
  select.select-input {
    width: 100%;
    padding: 15px;
    border: 1px solid #dadce0;
    border-radius: 4px;
    font-size: 16px;
    transition: border 0.3s;
    appearance: none;
    background-image: url("data:image/svg+xml;charset=UTF-8,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='%235f6368'%3e%3cpath d='M7 10l5 5 5-5z'/%3e%3c/svg%3e");
    background-repeat: no-repeat;
    background-position: right 10px center;
    background-size: 24px;
  }
  
  /* Verification Status */
  .verification-status {
    margin: 30px 0;
    padding: 15px;
    background-color: #fef7e0;
    border-radius: 8px;
    display: flex;
    align-items: center;
  }
  
  .status-icon {
    margin-right: 15px;
    font-size: 24px;
  }
  
  .status-text {
    font-size: 14px;
  }
  
  .pending {
    color: #f29900;
    font-weight: 500;
  }
  
  /* Media queries update */
  @media (max-width: 600px) {
    .verification-tabs {
      flex-direction: row;
    }
    
    .tab {
      flex: 1;
      text-align: center;
      padding: 12px 0;
    }
  }
  </style>