from flask import Flask, render_template, request, jsonify, redirect, url_for
import pickle
import re
import random
import os
from datetime import datetime
from collections import Counter
import json

app = Flask(__name__)
app.secret_key = 'cancer_cure_qa_secret_key_2024'

class CancerCureQASystem:
    def __init__(self):
        self.treatment_responses = {
            'herbal': [
                "by using black walnut hulls, wormwood, and cloves to eliminate parasites",
                "through herbal protocol with black walnut tincture daily for 3 weeks",
                "by taking wormwood capsules (200-300mg) and clove powder (500mg) combination",
                "using the complete herbal parasite cleanse with black walnut, wormwood, cloves",
                "by consuming fresh black walnut hulls and artemisia absinthium extract",
                "through natural herbs like black walnut hull and clove oil treatment regime"
            ],
            
            'electronic': [
                "by using electronic zapper device at specific frequencies (30kHz, 434kHz)",
                "through frequency generator targeting parasites at 434,000 Hz for 7 minutes",
                "by applying electronic current (9V, positive offset) to eliminate microorganisms",
                "using the zapper device with copper handles for 7 minutes, 3 times daily",
                "through bioelectronic therapy targeting pathogenic frequencies systematically",
                "by electronic parasite elimination using frequency-specific devices daily"
            ],
            
            'detox': [
                "by removing isopropyl alcohol and benzene from body through liver cleanse",
                "through liver detox (Epsom salt flush) and kidney cleanse programs monthly",
                "by eliminating heavy metals using chelation and natural detox protocols",
                "through dental cleanup removing all mercury amalgam fillings and root canals",
                "by detoxifying accumulated pollutants and carcinogens from tissues",
                "using colon cleanse with magnesium oxide and parasite elimination protocols"
            ],
            
            'nutrition': [
                "by eating only organic vegetables and avoiding all processed foods completely",
                "through proper nutrition eliminating artificial additives, dyes, and preservatives",
                "by consuming fresh organic fruits and raw foods rich in natural enzymes", 
                "using targeted nutritional supplements and immune-boosting vitamins daily",
                "through strict dietary changes removing all chemical preservatives and additives",
                "by following 100% organic diet free from pesticides, dyes, and chemicals"
            ],
            
            'parasite': [
                "by eliminating all intestinal flukes (Fasciolopsis buski) and parasitic worms",
                "through complete parasite cleanse targeting liver flukes causing cancer",
                "by removing parasites that produce ortho-phospho-tyrosine (cancer trigger)",
                "using combined antiparasitic herbs and electronic frequency treatment",
                "through systematic elimination of all parasites from liver, intestines, brain",
                "by targeting specific parasites in organs using herbs and zapper together"
            ],
            
            'environment': [
                "by removing all environmental toxins from living and working spaces",
                "through complete elimination of isopropyl alcohol from personal products",
                "by avoiding benzene, PCBs, formaldehyde and other carcinogenic chemicals",
                "using air purifiers, water filtration, and EMF protection systems",
                "through total household product replacement with natural alternatives",
                "by creating completely toxin-free environment for optimal healing"
            ]
        }
        
        self.question_patterns = {
            'cure': ['herbal', 'electronic', 'parasite'],
            'treat': ['herbal', 'electronic', 'detox'],
            'heal': ['nutrition', 'detox', 'herbal'],
            'eliminate': ['parasite', 'electronic', 'detox'],
            'remove': ['detox', 'parasite', 'environment'],
            'cleanse': ['detox', 'parasite', 'nutrition'],
            'natural': ['herbal', 'nutrition', 'environment'],
            'frequency': ['electronic'],
            'zapper': ['electronic'],
            'herbs': ['herbal'],
            'herbal': ['herbal'],
            'detox': ['detox', 'environment'],
            'parasite': ['parasite', 'electronic'],
            'organic': ['nutrition', 'environment'],
            'protocol': ['herbal', 'detox', 'electronic'],
            'device': ['electronic'],
            'supplement': ['nutrition'],
            'diet': ['nutrition', 'environment']
        }
        
        self.default_responses = [
            "by eliminating parasites using complete herbal cleanse and electronic zapper",
            "through systematic parasite elimination and comprehensive detoxification protocol",
            "by using black walnut, wormwood, cloves combined with frequency treatment",
            "through natural methods targeting root cause - parasites and environmental toxins",
            "by removing the fundamental cause: parasites and accumulated chemical toxins",
            "using holistic approach combining herbs, detox, and bioelectronic therapy"
        ]
        
        self.classifier = None
        self.vectorizer = None
        self.model_loaded = False
        self.question_count = 0
        self.category_stats = Counter()
    
    def load_model(self, model_path):
        try:
            if os.path.exists(model_path):
                with open(model_path, 'rb') as f:
                    model_package = pickle.load(f)
                self.classifier = model_package['best_model']
                self.vectorizer = model_package['vectorizer']
                self.model_loaded = True
                print(f"✅ ML Model loaded from: {model_path}")
                return True
            else:
                print(f"⚠️  Model file not found: {model_path}")
                return False
        except Exception as e:
            print(f"❌ Error loading model: {e}")
            return False
    
    def _preprocess_text(self, text):
        text = text.lower()
        text = re.sub(r'[^a-zA-Z\s]', ' ', text)
        text = ' '.join(text.split())
        return text
    
    def _extract_keywords(self, question):
        processed = self._preprocess_text(question)
        words = processed.split()
        matched_categories = []
        matched_keywords = []
        
        for word in words:
            for pattern, categories in self.question_patterns.items():
                if pattern in word or word in pattern:
                    matched_categories.extend(categories)
                    matched_keywords.append(pattern)
        
        return matched_categories, matched_keywords
    
    def _classify_question(self, question):
        if not self.model_loaded:
            return None, 0.0
        
        try:
            clean_text = self._preprocess_text(question)
            if not clean_text.strip():
                return None, 0.0
            
            text_vector = self.vectorizer.transform([clean_text])
            prediction = self.classifier.predict(text_vector)[0]
            
            confidence = 0.0
            if hasattr(self.classifier, 'predict_proba'):
                probabilities = self.classifier.predict_proba(text_vector)[0]
                confidence = max(probabilities)
            
            return prediction, confidence
            
        except Exception as e:
            print(f"Classification error: {e}")
            return None, 0.0
    
    def generate_response(self, question):
        self.question_count += 1
        
        response_data = {
            'question': question,
            'timestamp': datetime.now().isoformat(),
            'question_id': self.question_count
        }
        
        ml_category, ml_confidence = self._classify_question(question)
        response_data['ml_classification'] = {
            'category': ml_category,
            'confidence': round(ml_confidence, 4) if ml_confidence else 0.0,
            'model_used': self.model_loaded
        }
        
        keyword_categories, matched_keywords = self._extract_keywords(question)
        response_data['keyword_analysis'] = {
            'matched_keywords': matched_keywords,
            'suggested_categories': keyword_categories
        }
        
        all_categories = []
        
        if ml_category:
            if 'treatment' in ml_category.lower():
                all_categories.extend(['herbal', 'electronic'])
            elif 'pathogen' in ml_category.lower():
                all_categories.extend(['parasite', 'electronic'])
            elif 'detox' in ml_category.lower():
                all_categories.extend(['detox', 'environment'])
            elif 'nutrition' in ml_category.lower():
                all_categories.append('nutrition')
            elif 'research' in ml_category.lower():
                all_categories.extend(['herbal', 'electronic'])
            elif 'medical' in ml_category.lower():
                all_categories.extend(['herbal', 'parasite'])
        
        all_categories.extend(keyword_categories)
        
        if all_categories:
            category_counts = Counter(all_categories)
            best_category = category_counts.most_common(1)[0][0]
            response = random.choice(self.treatment_responses[best_category])
            
            response_data['selected_approach'] = best_category
            response_data['category_scores'] = dict(category_counts)
        else:
            best_category = 'default'
            response = random.choice(self.default_responses)
            response_data['selected_approach'] = 'default'
            response_data['category_scores'] = {}
        
        response_data['treatment_response'] = response
        self.category_stats[best_category] += 1
        
        return response_data

qa_system = CancerCureQASystem()

# Ensure models directory exists
if not os.path.exists('models'):
    os.makedirs('models')

MODEL_PATH = os.path.join("models", "cure_cancer_text_classifier_20250816_195229.pkl")
qa_system.load_model(MODEL_PATH)

@app.route('/')
def home():
    return render_template('index.html', 
                         model_loaded=qa_system.model_loaded,
                         question_count=qa_system.question_count)

@app.route('/ask', methods=['POST'])
def ask_question():
    try:
        data = request.get_json()
        question = data.get('question', '').strip()
        
        if not question:
            return jsonify({
                'success': False,
                'error': 'Please enter a question'
            })
        
        response_data = qa_system.generate_response(question)
        
        return jsonify({
            'success': True,
            'data': response_data
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Server error: {str(e)}'
        })

@app.route('/stats')
def statistics():
    stats_data = {
        'total_questions': qa_system.question_count,
        'model_loaded': qa_system.model_loaded,
        'category_distribution': dict(qa_system.category_stats),
        'model_path': MODEL_PATH
    }
    
    return render_template('stats.html', stats=stats_data)

@app.route('/api/stats')
def api_stats():
    return jsonify({
        'total_questions': qa_system.question_count,
        'model_loaded': qa_system.model_loaded,
        'category_stats': dict(qa_system.category_stats)
    })

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    if not os.path.exists('templates'):
        os.makedirs('templates')
    if not os.path.exists('static'):
        os.makedirs('static')
    app.run(debug=True)
