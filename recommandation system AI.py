import pandas as pd
data = {
    'Destination': [
        'Paris, France', 
        'Grand Canyon, USA', 
        'Bali, Indonesia', 
        'Machu Picchu, Peru', 
        'Rome, Italy', 
        'Maldives', 
        'Great Wall of China, China', 
        'Banff National Park, Canada'
    ],
    'Type': [
        'Historical Cultural', 
        'Adventure Scenic', 
        'Beach Adventure', 
        'Historical Adventure', 
        'Historical Cultural', 
        'Beach Relaxation', 
        'Historical Scenic', 
        'Adventure Scenic'
    ]
}
df = pd.DataFrame(data)

def recommend_trips_by_type(user_input, df):
    print(f"\nYour preferred trip type: {user_input}")  
    sim_scores = []
    for index, row in df.iterrows():
        trip_type = row['Type']
        common_keywords = len(set(user_input.lower().split()) & set(trip_type.lower().split()))
        sim_scores.append((index, common_keywords))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)  
    recommended_indices = [score[0] for score in sim_scores if score[1] > 0][:3]    
    if recommended_indices:
        print("\nTrips recommended for you based on trip type similarity:")
        for idx in recommended_indices:
            print(f"- {df['Destination'][idx]} ({df['Type'][idx]})")
    else:
        print("\nNo matching trips found. Try a different trip type.")

user_input = input("Enter your preferred trip type (e.g., 'Beach', 'Adventure', 'Historical', 'Cultural'): ")
recommend_trips_by_type(user_input, df)
