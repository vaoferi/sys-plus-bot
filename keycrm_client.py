"""
KeyCRM API Client
Клієнт для роботи з KeyCRM API
"""

import aiohttp
import logging
from typing import List, Dict, Optional

logger = logging.getLogger(__name__)


class KeyCRMClient:
    """Клієнт для взаємодії з KeyCRM API"""
    
    def __init__(self, api_key: str, base_url: str = 'https://keycrm.app/api/v2'):
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }
    
    async def _request(self, method: str, endpoint: str, data: Optional[Dict] = None) -> Dict:
        """Виконати HTTP запит до KeyCRM API"""
        url = f"{self.base_url}/{endpoint}"
        
        async with aiohttp.ClientSession() as session:
            async with session.request(method, url, headers=self.headers, json=data) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    error_text = await response.text()
                    logger.error(f"API Error {response.status}: {error_text}")
                    raise Exception(f"KeyCRM API Error: {response.status}")
    
    async def get_recent_orders(self, limit: int = 10) -> List[Dict]:
        """Отримати останні замовлення"""
        try:
            result = await self._request('GET', f'orders?limit={limit}')
            return result.get('data', [])
        except Exception as e:
            logger.error(f"Error fetching orders: {e}")
            return []
    
    async def get_order_by_id(self, order_id: int) -> Optional[Dict]:
        """Отримати замовлення по ID"""
        try:
            result = await self._request('GET', f'orders/{order_id}')
            return result.get('data')
        except Exception as e:
            logger.error(f"Error fetching order {order_id}: {e}")
            return None
    
    async def get_recent_clients(self, limit: int = 10) -> List[Dict]:
        """Отримати останніх клієнтів"""
        try:
            result = await self._request('GET', f'clients?limit={limit}')
            return result.get('data', [])
        except Exception as e:
            logger.error(f"Error fetching clients: {e}")
            return []
    
    async def get_client_by_id(self, client_id: int) -> Optional[Dict]:
        """Отримати клієнта по ID"""
        try:
            result = await self._request('GET', f'clients/{client_id}')
            return result.get('data')
        except Exception as e:
            logger.error(f"Error fetching client {client_id}: {e}")
            return None
    
    async def get_statistics(self) -> Dict:
        """Отримати базову статистику"""
        try:
            # Отримуємо замовлення для підрахунку статистики
            orders = await self.get_recent_orders(limit=100)
            clients = await self.get_recent_clients(limit=100)
            
            total_revenue = sum(order.get('total', 0) for order in orders)
            
            return {
                'total_orders': len(orders),
                'total_revenue': total_revenue,
                'total_clients': len(clients)
            }
        except Exception as e:
            logger.error(f"Error fetching statistics: {e}")
            return {
                'total_orders': 0,
                'total_revenue': 0,
                'total_clients': 0
            }
    
    async def update_order_status(self, order_id: int, status: str) -> bool:
        """Оновити статус замовлення"""
        try:
            data = {'status': status}
            await self._request('PUT', f'orders/{order_id}', data=data)
            return True
        except Exception as e:
            logger.error(f"Error updating order status: {e}")
            return False
    
    async def create_note(self, entity_type: str, entity_id: int, note: str) -> bool:
        """Створити нотатку для замовлення або клієнта"""
        try:
            data = {
                'entity_type': entity_type,
                'entity_id': entity_id,
                'text': note
            }
            await self._request('POST', 'notes', data=data)
            return True
        except Exception as e:
            logger.error(f"Error creating note: {e}")
            return False
