### Mental-Health-Advice

**Project Title:** Mental-Health-Advice

**Industry:** Healthcare

**Project Description:**  
Mental-Health-Advice is an innovative online platform designed to provide instant, accessible mental health support through a user-friendly chat interface. This platform addresses the critical need for continuous, typical mental health advice and support, especially for individuals experiencing conditions such as panic attacks, headaches, pain, loneliness, low self-esteem, anxiety, stress, depression, and many more. The platform operates 24/7, ensuring users can access help anytime and anywhere, thus breaking the barriers of time and location that traditionally hinder access to mental health care.

**Key Features:**

- **24/7 Availability:** Users can access mental health advice and support anytime, from anywhere.
- **Typical Therapeutic Techniques:** Provides advice based on established therapeutic methods.
- **User-Friendly Chat Interface:** Easy-to-use chat interface for seamless interaction.
- **Natural Language Processing:** Utilizes advanced NLP models to understand and respond to user queries effectively.

**Technologies Used:**

- **Website Development:** HTML, CSS, JavaScript, Bootstrap
- **Backend Framework:** Flask

**Azure Services Utilized:**

- **Azure App Service:** Hosts the web application, ensuring it is scalable, secure, and always available.
- **Azure Language Service:** Implements the Conversational Language Understanding model and Custom Question Answering model to process and understand user inputs in natural language.
- **Azure Storage Account:** Stores user data and application files securely, ensuring data integrity and availability.
- **Azure Bot Service:** Powers the chat interface, enabling real-time communication between users and the application.
- **Azure AI Search Service:** Utilized for indexing and searching the Custom Question Answering knowledge base, ensuring efficient retrieval of relevant answers.

**Azure Language Studio:**
- **Conversational Language Understanding Model:** Analyzes and interprets user inputs to identify the user's intent and provide appropriate responses.
- **Custom Question Answering Model:** Provides precise answers to user queries by leveraging a knowledge base of mental health information.

**Interconnection of Azure Services:**

**My Resource Group**
![Screenshot 2024-06-08 121529](https://github.com/Barun-me/Mental-Health-Advice/assets/156335152/935ea104-a1ab-42b5-bd74-390c80d07894)

1. **Azure App Service:** Acts as the central hub, hosting the web application and managing requests from users. ![Screenshot 2024-06-08 123228](https://github.com/Barun-me/Mental-Health-Advice/assets/156335152/d1e37072-f191-4b7a-b9d0-ad27fcfc73bd)
![Screenshot 2024-06-08 121652](https://github.com/Barun-me/Mental-Health-Advice/assets/156335152/dcc476aa-2377-4391-85c6-6af4f9f9a536)
![Screenshot 2024-06-08 123047](https://github.com/Barun-me/Mental-Health-Advice/assets/156335152/160adc7c-8f97-4b65-a9e6-a99986c345e2)
![Screenshot 2024-06-08 152801](https://github.com/Barun-me/Mental-Health-Advice/assets/156335152/f7a58a40-e340-43b0-9d2f-4042e480b6d9)
![Screenshot 2024-06-08 131621](https://github.com/Barun-me/Mental-Health-Advice/assets/156335152/49aa5912-f845-4458-8bf1-d427d638f4c9)
![Screenshot 2024-06-08 131752](https://github.com/Barun-me/Mental-Health-Advice/assets/156335152/f13d0236-537a-4f98-ad10-f167171bd25b)
![Screenshot 2024-06-08 131806](https://github.com/Barun-me/Mental-Health-Advice/assets/156335152/029d9a45-f04a-46ee-8426-b57eb8e52276)
![Screenshot 2024-06-08 131826](https://github.com/Barun-me/Mental-Health-Advice/assets/156335152/539dadf7-537c-4902-b590-edffcb2ed6e3)
**Mental Health Advice Chat Interface**
![Screenshot 2024-06-08 152708](https://github.com/Barun-me/Mental-Health-Advice/assets/156335152/93c9c92a-f041-4ba4-aa84-2b1ebc73789c)


2. **User Interaction:** When a user interacts with the chat interface, the input is sent to the Azure Bot Service.![Screenshot 2024-06-08 121902](https://github.com/Barun-me/Mental-Health-Advice/assets/156335152/d9c75018-e423-4e28-9e39-3b527a4cccb8)

3. **Input Processing:** The Azure Bot Service processes the input and sends it to the Azure Language Service.![Screenshot 2024-06-08 123459](https://github.com/Barun-me/Mental-Health-Advice/assets/156335152/adfac72e-d64c-42ee-a81e-694296cf6689)

4. **Intent Analysis:** The Conversational Language Understanding Model analyzes the input to determine the user's intent.![Screenshot 2024-06-08 123538](https://github.com/Barun-me/Mental-Health-Advice/assets/156335152/c6083504-6850-4f48-ab48-a2e3824a9a71)
![Screenshot 2024-06-07 132749](https://github.com/Barun-me/Mental-Health-Advice/assets/156335152/9c18c406-2a50-4aa8-b4e9-128d4a8ea79a)

5. **Answer Retrieval:** The Custom Question Answering Model, leveraging Azure AI Search Service, searches for the best possible response based on the knowledge base.![Screenshot 2024-06-07 132842](https://github.com/Barun-me/Mental-Health-Advice/assets/156335152/3c712646-1774-4741-9c2f-7691fd3f30e8)
![Screenshot 2024-06-08 124109](https://github.com/Barun-me/Mental-Health-Advice/assets/156335152/d3f9e8da-f46f-426f-b392-b90f3184c8f5)

6. **Response Delivery:** Once the appropriate response is identified, it is sent back through the Azure Bot Service to the user.![Screenshot 2024-06-08 121902](https://github.com/Barun-me/Mental-Health-Advice/assets/156335152/82723024-d040-4c37-bd37-22d21b95f50c)

7. **Data Management:** All data and application files are securely stored and managed using the Azure Storage Account, ensuring the system's reliability and data security.
![Screenshot 2024-06-08 124143](https://github.com/Barun-me/Mental-Health-Advice/assets/156335152/3c2ea446-c74c-4a34-8bdd-e014a055a8fc)

**Project Impact:**  
Mental-Health-Advice aims to bridge the gap in mental health services by providing immediate advice. By leveraging Azure's powerful services, the platform ensures that users receive accurate and timely advice, fostering a supportive environment for individuals struggling with common mental health issues.

---
