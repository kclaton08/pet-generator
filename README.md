# pet-generator

<h1>Pet Generator</h1>
<p>Summary: Pet Generator is an application that allows you to create your own collection of pets. You can choose from cats and dogs and even give them their own names!</p>

<h2>How to run appliction</h2>
<p>
    1. Clone repository locally and run "pip install -r requirements.txt" when you are in the root directory of pet-generator. This will install all of the application dependencies"
</p>

<p>
    2. Navigate to app.py within pet-generator/src/appication/app.py and run in a dedicated terminal. This will start the application on localhost:8000 or the port of your choice. To go to the application, navigate to http://localhost:8000/pet-generator. This will bring you to the frontend where you can start generating your collection of pets! 
</p>

<p>
    3. To containerize the application, you can run "docker build -t my_app:1.0.0 ." while you have a docker engine running on your local computer. This will buid the application utilizing a linux image.
</p>

<h2>Using the REST API endpoint</h2>
<p>
    Pet Generator comes with an endpoint that allows you to retrieve all of your pets within your collection!. To do so, you can leverage the /pet-repository endpoint. 

    Furthermore, you can pass the following query query parameters:

        limit={1-1000} to retrieve an exact amount of your pets
        animal_type={cat or dog} 
</p>