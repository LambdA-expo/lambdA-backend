# Backend for MVP

## Branching Rules 
- for creating new feature :  `feature/<feature_name>`
- bug fixing : `bugFix/<bug_name>`
- hotfix : `hotfix/<hotfix_name>`

Terms : 
    - Franchisor -> who wants to sell his business to an individual
    - Franchise or Buyer -> who want to buy rights to open a franchisor's business

MVP Features :
    
    a. feature/login-signup : login and signup for both Franchisor and Buyers
    b. feature/otp-verifcation : otp verification common for both login and signup 
    c. feature/franchise-connection : connection/interested request to franchisor
    d. feature/enable-chat-app: enabling chat application

**Buyer/Franchise Side:**
    1. Buyer browses Franchisors from the **Franchisor Table**.
    2. On viewing a specific Franchisor, they see the requirements and questions.
    3. The buyer submits their interest via the **Interest Table**, providing:
       - Answers to any questions (stored in the `responses` field)
    4. After submission, their interest is set to "Pending" and they wait for approval.

**Franchisor Owner Side:**
    1. Franchisor owner lists a Franchisor in the **Franchisor Table** with requirements and custom questions.
    2. They can view an approval dashboard, showing all **interested buyers** from the **Interest Table**.
    3. Once they approve a buyer's request, the `status` in the **Interest Table** changes to "Approved."
   
**Chat Application**
    1. If Franchisor owner approves buyer request then enable chat application for both buyer and Franchisor.


# DATABASE SCHEMA
To implement this functionality, we need to capture additional details such as franchise requirements, buyer responses, approval status, and a chat feature. Here's how the schema could be structured:

## Tables:

## 1. **Users Table**
- `user_id` (Primary Key)
- `name`
- `email`
- `phone`
- `user_type` (Enum: Franchisor, Buyer)
- `is_otp_verified`
- `created_at`
- `updated_at`

## 2. **Franchisor Table**
- `franchisor_id` (Primary Key)
- `user_id` (Foreign Key referencing Users) – Franchisor owner who posted the listing
- `franchisor_name`
- `company_name`
- `owner_name`
- `owner_email`
- `owner_mobile_number`
- `manager_name`
- `address`
- `country`
- `pincode`
- `state`
- `city`
- `gst_number`
- `website_url`
- `video_url`
- `logo_url`
- `description`
- `category_id` :  f.k referencing category
- `sub_category_id` : f.k referencing sub category
- `service_id` : f.k referencing service
- `meta_data` (JSON field for storing requirements)
- `questions` (JSON field for questions the owner wants the buyer to answer)
- `created_at`
- `updated_at`

## 3. **Buyer Table**
- `buyer_id` (Primary Key)
- `user_id` (Foreign Key referencing Users)  
- `name`
- `contact_email`
- `contact_phone`
- `date_of_birth`
- `address`
- `country`
- `state`
- `city`
- `pincode`
- `meta_data` : (JSON field for storing requirements)
- `created_at`
- `updated_at`


## 4. **Interest Request Table** (Captures buyer interest and their response to franchisor requirements)
- `interest_id` (Primary Key)
- `buyer_id` (Foreign Key referencing Buyer)
- `franchisor_id` (Foreign Key referencing Franchisor)
- `responses` (JSON field for buyer's answers to the questions asked by the franchise owner, investment budget)
- `submitted_at`
- `approval_status` (Enum: Pending, Approved, Rejected)


## 5. **Category Table** or **Industry Table**  (One Category/Industry can have many multiple subcategory)
- `category_id`
- `category_name`
- `created_at`
- `updated_at`

## 6. **Sub Category Table** or **Sub Industry Table**  (Many SubCategory/Industry can have one category)
- `sub_category_id`
- `category_id`
- `sub_category_name`
- `created_at`
- `updated_at`

## 7. **Service/Product Table** (Many Service/Product can have one Subcategory)
- `service_id`
- `sub_category_id`
- `service_name`
- `created_at`
- `updated_at`

## TTL (Time-to-Live) for OTPs: automate the deletion of expired OTPs using TTL (Time-to-Live) features in your database, which will automatically remove expired entries to keep the table clean.
## 8. **OTP Table**
- `otp_id`
- `user_id`
- `otp_code`
- `is_used`
- `expires_at`	
- `created_at`	
- `updated_at`